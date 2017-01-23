# coding=utf-8

from views import BaseHandler
from models.user import User
from models.post import Post
from models.comment import Comment
from playhouse.shortcuts import model_to_dict, dict_to_model
from exceptions.json import *
from kit.auth import auth_login

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
        self.fill_users([post_dict])
        self.finish_json(result={
            'post': post_dict
            })

    @auth_login
    def get(self):
        start_id = int(self.get_argument('start_id', -1))
        limit = int(self.get_argument('limit', 20))
        if start_id != -1:
            posts = Post.select().where(Post.id < start_id).order_by(-Post.created_at).limit(limit)
        else:
            posts = Post.select().order_by(-Post.created_at).limit(limit)
        posts_dict = [post.to_dict() for post in posts]
        self.fill_comments(posts_dict)
        self.fill_users(posts_dict)
        self.finish_json(result={
            'posts': posts_dict
            })

    def fill_users(self, posts):
        user_ids = []
        for post in posts:
            if post['author_id'] not in user_ids:
                user_ids.append(post['author_id'])
            if post['target_id'] not in user_ids:
                user_ids.append(post['target_id'])
            for comment in post.get('comments', []):
                if comment['author_id'] not in user_ids:
                    user_ids.append(comment['author_id'])

        users_db = User.select().where(User.id << user_ids)
        users = [user.to_dict() for user in users_db]
        for post in posts:
            post['target'] = self.get_user_by_id(users, post['target_id'])
            post['author'] = self.get_user_by_id(users, post['author_id'])
            for comment in post.get('comments', []):
                comment['author'] = self.get_user_by_id(users, comment['author_id'])


    def get_user_by_id(self, users, id):
        try:
            return  next(user for user in users if user['id'] == id)
        except:
            pass


    def fill_comments(self, posts):
        post_ids = [post['id'] for post in posts]
        comments = Comment.select().where(Comment.post_id << post_ids)
        for post in posts:
            post['comments'] = [comment.to_dict() for comment in comments if comment.post_id == post['id']]
