# -*- coding: utf-8 -*-

from peewee import *
from models import db, BaseModel
import hashlib

class User(BaseModel):

    id = IntegerField()
    username = CharField()
    email = CharField()
    password = CharField()
    enable = IntegerField()
    avatar = CharField()

    def to_dict(self):
        r = super().to_dict()
        del r['password']
        # if self.email is not None:
            # r['avatar'] = "https://www.gravatar.com/avatar/" + hashlib.md5(self.email.encode('utf-8')).hexdigest()
        return r

