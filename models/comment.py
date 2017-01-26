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
