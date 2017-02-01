# -*- coding: utf-8 -*-

from peewee import *
from models import db, BaseModel
from kit.config import config

class Auth(BaseModel):

    id = IntegerField()
    source_id = IntegerField()
    user_id = IntegerField()
    access_token = CharField()

salt = config['user_password_salt']
