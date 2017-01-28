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
        comment_dict = comment.to_dict()
        comment_dict['author'] = self.current_user.to_dict()
        self.finish_json(result={
            "comment": comment_dict
            })


    @auth_login
    def delete(self, post_id, comment_id):
        comment = Comment.single(Comment.id == comment_id)
        if comment is None:
            raise JsonException(errcode=1001, errmsg="comment not exist")
        if comment.author_id != self.current_user.id:
            raise JsonException(errcode=1002, errmsg="permission not allow")
        comment.deleted = 1
        comment.save()
        self.finish_json()
