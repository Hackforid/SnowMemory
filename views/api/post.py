# coding=utf-8

from views import BaseHandler
from models.user import User
from models.post import Post
from models.comment import Comment
from playhouse.shortcuts import model_to_dict, dict_to_model
from exceptions.json import *
from kit.auth import auth_login
from kit.post import fill_user_and_comment_to_post

class PostHandler(BaseHandler):

    @auth_login
    def post(self):
        args = self.get_json_arguments()

        target_name = self.get_json_argument('target_name')
        photos = self.get_json_argument('photos')
        content = self.get_json_argument('content', '')

        target_user = User.single(User.username == target_name)
        if target_user is None:
            raise JsonException(errcode=1000, errmsg="target not exist")

        post = Post(author_id = self.current_user.id,
                target_id = target_user.id, photos = photos,
                content = content)
        post.save()
        post_dict = post.to_dict()
        post_dict['comments'] = []
        fill_user_and_comment_to_post([post_dict])
        self.finish_json(result={
            'post': post_dict
            })

    @auth_login
    def get(self):
        start_id = int(self.get_argument('start_id', -1))
        limit = int(self.get_argument('limit', 20))
        posts = Post.get_more(start_id, limit)
        posts_dict = [post.to_dict() for post in posts]
        fill_user_and_comment_to_post(posts_dict)
        self.finish_json(result={
            'posts': posts_dict
            })

class PostDetailHandler(BaseHandler):

    @auth_login
    def delete(self, post_id):
        post = Post.single(Post.id == post_id)
        if post is None:
            raise JsonException(errcode="1001", errmsg="Post not exist")
        if post.author_id != self.current_user.id:
            raise JsonException(errcode="1002", errmsg="Permission not allowed")
        post.deleted = 1
        post.save()
        self.finish_json()

    @auth_login
    def get(self, post_id):
        post = Post.single(Post.id == post_id)
        if post is None:
            raise JsonException(errcode="1001", errmsg="Post not exist")
        post_dict = post.to_dict()
        fill_user_and_comment_to_post([post_dict])

        self.finish_json(result={
            'post': post_dict
            })
