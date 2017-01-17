# -*- coding: utf-8 -*-

from views import BaseHandler
from models.user import User
from playhouse.shortcuts import model_to_dict, dict_to_model
from exceptions.json import *
from kit.auth import auth_login

class UserHandler(BaseHandler):

    @auth_login
    def get(self, id):
        user = User.get(User.id == id)
        print(user.to_dict())
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
        if 'nickname' in user_dict:
            user.nickname = user_dict['nickname']

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

