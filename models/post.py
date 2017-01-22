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
