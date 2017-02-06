# -*- coding: utf-8 -*-

from peewee import *
from models import db, BaseModel

class CharArrayField(Field):

    db_field = 'varchar'

    def db_value(self, value):
        str = '::'.join(value)
        return str

    def python_value(self, value):
        return value.split("::")

class Post(BaseModel):

    id = IntegerField()
    author_id = IntegerField()
    target_id = IntegerField()
    content = CharField()
    photos = CharArrayField()
    created_at = DateTimeField()
    deleted = IntegerField()

    @staticmethod
    def get_more(start_id=-1, limit=20):
        if start_id != -1:
            posts = Post.select().where(Post.id < start_id, Post.deleted != 1).order_by(-Post.created_at).limit(limit)
        else:
            posts = Post.select().where(Post.deleted != 1).order_by(-Post.created_at).limit(limit)
        return posts

    @staticmethod
    def get_by_user(user_id):
        posts = Post.select().where(Post.target_id == user_id, Post.deleted != 1).order_by(-Post.created_at)
        return posts
