# -*- coding: utf-8 -*-

from peewee import *
from models import db, BaseModel

class Auth(BaseModel):

    id = IntegerField()
    source_id = IntegerField()
    user_id = IntegerField()
    access_token = CharField()

salt = 'test_salt_*(A&J2335HGJ-KHGS0A^HGJHKG)'
