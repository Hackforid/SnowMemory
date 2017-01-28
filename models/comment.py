# -*- coding: utf-8 -*-

from peewee import *
from models import db, BaseModel

class Comment(BaseModel):
    id = IntegerField()
    author_id = IntegerField()
    post_id = IntegerField()
    content = CharField()
    created_at = DateTimeField()
    deleted = IntegerField()

    @staticmethod
    def get_by_post_ids(post_ids):
        return Comment.select().where(Comment.post_id << post_ids, Comment.deleted == 0)

