# -*- coding: utf-8 -*-

from views import BaseHandler
from models.user import User
from models.post import Post
from models.auth import Auth
from playhouse.shortcuts import model_to_dict, dict_to_model
from exceptions.json import *
from kit.auth import auth_login, password_hash, gen_access_token
from kit.post import fill_user_and_comment_to_post
from utils.json import json_encode
from models import db

class UserHandler(BaseHandler):

    @auth_login
    def get(self, id):
        user = User.get(User.id == id)
        self.write(user.to_dict())

    def post(self):
        user_dict = self.get_json_arguments()
        user = dict_to_model(User, user_dict)
        user.save()
        self.write(user.to_dict())

    def put(self, id):
        user_dict = self.get_json_arguments()
        user = User.get(User.id == id)
        if not user:
            raise JsonException(1000, "user not exist")
        if 'username' in user_dict:
            user.username = user_dict['username']
        if 'password' in user_dict:
            user.password = user_dict['password']

        user.save()
        self.write(user.to_dict())

    def delete(self, id):
        user = User.get(User.id == id)
        if not user:
            raise JsonException(1000, "user not exist")
        user.enable = 0
        user.save()
        self.write(user.to_dict())


class UsersHandler(BaseHandler):

    @auth_login
    def get(self):
        users = User.select()
        self.finish_json(result={
            'users': [user.to_dict() for user in users]
            })

class UserInfoHandler(BaseHandler):

    @auth_login
    def get(self, username):
        user = User.single(User.username == username)
        if user is None:
            raise JsonException(errcode=1001, errmsg="")
        posts = Post.select().where(Post.target_id == user.id)
        posts_dict = [post.to_dict() for post in posts]
        print(json_encode(posts_dict))
        fill_user_and_comment_to_post(posts_dict)

        self.finish_json(result={
            "user": user.to_dict(),
            "posts": posts_dict
            })


class ChangeUsernameHandler(BaseHandler):

    @auth_login
    def put(self):
        username = self.get_json_argument('username')
        username = username.strip()
        if self.current_user.username == username:
            raise JsonException(errcode=1003, errmsg="username not changed")

        _user = User.single(User.username == username)
        if _user is not None:
            raise JsonException(errcode=1001, errmsg="username exist")

        db.begin()
        # change username
        self.current_user.username = username
        self.current_user.save()

        # change auth
        access_token = gen_access_token()
        auth = Auth.single(Auth.source_id==0, Auth.user_id==self.current_user.id)
        if auth is not None:
            auth.access_token = access_token
        else:
            auth = Auth(source_id=0, user_id=self.current_user.id, access_token=access_token)
        auth.save()

        db.commit()

        self.finish_json(result={
            "user": self.current_user.to_dict(),
            "access_token": access_token
            })

class ChangePasswordHandler(BaseHandler):

    @auth_login
    def put(self):
        old_password = self.get_json_argument('old_password').strip()
        new_password = self.get_json_argument('new_password').strip()

        saved_old_pwd = password_hash(old_password)
        if self.current_user.password != saved_old_pwd:
            raise JsonException(errcode="1001", errmsg="wrong pwd")

        self.current_user.password = password_hash(new_password)
        self.current_user.save()
        self.finish_json(result={
            "user": self.current_user.to_dict()
            })



