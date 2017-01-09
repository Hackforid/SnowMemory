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
