# coding=utf-8

from views import BaseHandler
from models.user import User
from models.post import Post
from playhouse.shortcuts import model_to_dict, dict_to_model
from exceptions.json import *

class PostHandler(BaseHandler):

    def post(self):
        args = self.get_json_arguments()

        author_id = args['author_id']
        target_id = args['target_id']
        photos = args['photos']
        content = args['content']

        post = Post(author_id = author_id,
                target_id = target_id,
                photos = photos,
                content = content)
        post.save()
        self.finish_json(result={
            'post': post.to_dict()
            })

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
            post['target'] = next(user for user in users if user.id == post['target_id']).to_dict()
            post['author'] = next(user for user in users if user.id == post['author_id']).to_dict()


