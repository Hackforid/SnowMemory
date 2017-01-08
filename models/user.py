# -*- coding: utf-8 -*-

from peewee import *
from models import db, BaseModel

class User(BaseModel):

    id = IntegerField()
    username = CharField()
    password = CharField()
    nickname = CharField()
    enable = IntegerField()

    class Meta:
        database = db
