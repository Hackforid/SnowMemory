# coding=utf-8

from views import BaseHandler
from models.user import User
from models.post import Post
from playhouse.shortcuts import model_to_dict, dict_to_model
from exceptions.json import *
from kit.auth import auth_login

class PostHandler(BaseHandler):

    @auth_login
    def post(self):
        args = self.get_json_arguments()

        target_name = args['target_name']
        photos = args['photos']
        content = args['content']

        target_user = User.single(User.username == target_name)
        if target_user is None:
            raise JsonException(errcode=1000, errmsg="target not exist")

        post = Post(author_id = self.current_user.id,
                target_id = target_user.id,
                photos = photos,
                content = content)
        post.save()
        self.finish_json(result={
            'post': post.to_dict()
            })

    @auth_login
    def get(self):
        posts = Post.select()
        posts_dict = [post.to_dict() for post in posts]
        self.fill_users(posts_dict)
        self.finish_json(result={
            'list': posts_dict
            })

    def fill_users(self, posts):
        user_ids = []
        for post in posts:
            print(post)
            if post['author_id'] not in user_ids:
                user_ids.append(post['author_id'])
            if post['target_id'] not in user_ids:
                user_ids.append(post['target_id'])
        users = User.select().where(User.id << user_ids)
        for post in posts:
            try:
                post['target'] = next(user for user in users if user.id == post['target_id']).to_dict()
            except:
                pass

            try:
                post['author'] = next(user for user in users if user.id == post['author_id']).to_dict()
            except:
                pass


