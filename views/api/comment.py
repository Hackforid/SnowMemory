# coding=utf-8

from views import BaseHandler
from models.user import User
from models.post import Post
from models.comment import Comment
from playhouse.shortcuts import model_to_dict, dict_to_model
from exceptions.json import *
from kit.auth import auth_login

class CommentHandler(BaseHandler):

    @auth_login
    def post(self, post_id):
        args = self.get_json_arguments()
        content = args['content']
        
        comment = Comment(post_id = post_id,
                author_id = self.current_user.id,
                content = content
                )
        comment.save()
        self.finish_json(result={
            "comment": comment.to_dict()
            })


