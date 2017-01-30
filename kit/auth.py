# coding=utf-8

import hashlib
import datetime
from models.auth import salt

def password_hash(password):
    password_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return password_hash

def auth_login(fn):
    def _(self, *args, **kwargs):

        if self.current_user:
            return fn(self, *args, **kwargs)
        else:
            self.finish_json(errcode=3000, errmsg="need login")
    return _

def gen_access_token():
    access_token = password_hash(str(datetime.datetime.now()))
    return access_token
