# coding=utf-8

import hashlib
import datetime

from views import BaseHandler
from models.user import User
from models.auth import Auth
from playhouse.shortcuts import model_to_dict, dict_to_model
from exceptions.json import *
from kit.auth import password_hash

class AuthHandler(BaseHandler):

    def post(self):
        args = self.get_json_arguments()
        source = int(args.get("source_id", 0))
        username = args['username']
        password = args['password']

        if not username or not password:
            raise JsonException(1000, 'need username and password')

        pwd = password_hash(password)
        try:
            user = User.get(User.username == username)
        except:
            user = None
        if user is None or user.password != pwd:
            raise JsonException(1001, 'wrong password')
        access_token = get_auth()
        auth = Auth.single(Auth.source_id == source and Auth.user_id == user.id)
        if auth is None:
            auth = Auth(source_id=source, user_id=user.id)
        auth.access_token = access_token
        auth.save()

        self.finish_json(result={
            'username': user.username,
            'id': user.id,
            'access_token': access_token
            })



class RegisterHandler(BaseHandler):

    def post(self):
        args = self.get_json_arguments()
        username = args['username']
        password = args['password']
        if not username or not password:
            raise JsonException(1000, 'need username and password')


        user = User.select().where(User.username == username).limit(1)
        if len(user) > 0:
            raise JsonException(10001, 'username exist')

        hashed_password = password_hash(password)

        user = User(username = username, password = hashed_password)
        user.save()
        access_token = get_auth()
        auth = Auth(source_id=0, user_id=user.id, access_token=access_token)
        auth.save()
        self.finish_json(result={
            'username': user.username,
            'id': user.id,
            'access_token': access_token
            })



def get_auth():
    access_token = password_hash(str(datetime.datetime.now()))
    return access_token

