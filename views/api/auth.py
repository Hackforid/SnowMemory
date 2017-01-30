# coding=utf-8

import hashlib
import datetime

from views import BaseHandler
from models.user import User
from models.auth import Auth
from playhouse.shortcuts import model_to_dict, dict_to_model
from exceptions.json import *
from kit.auth import password_hash, gen_access_token
from kit.redis import redis
from kit.mail import send_register_code
import utils.strings as strings


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
        access_token = gen_access_token()
        auth = Auth.single(
            Auth.source_id == source and Auth.user_id == user.id)
        if auth is None:
            auth = Auth(source_id=source, user_id=user.id)
        auth.access_token = access_token
        auth.save()

        self.finish_json(result={
            'user': user.to_dict(),
            'access_token': access_token
        })


class RegisterHandler(BaseHandler):

    async def post(self):
        username = self.get_json_argument('username')
        password = self.get_json_argument('password')
        email = self.get_json_argument('email')
        code = self.get_json_argument('code')

        # check user exist
        user = User.select().where(User.username == username or User.email == email).limit(1)
        if len(user) > 0:
            raise JsonException(10001, 'username of email exist')

        # check verify code
        key = self.gen_verify_code_key(email)
        verify_code = await redis.get(key)
        verify_code = str(verify_code, 'utf-8')
        #print(f"veri={verify_code} input={code}")
        if verify_code != code:
            raise JsonException(10002, 'verify code is incorrect')

        hashed_password = password_hash(password)
        user = User(username=username, password=hashed_password, email=email)
        user.save()
        access_token = gen_access_token()
        auth = Auth(source_id=0, user_id=user.id, access_token=access_token)
        auth.save()
        self.finish_json(result={
            "user": user.to_dict(),
            'access_token': access_token
        })

    async def get(self):
        email = self.get_argument('email')
        user = User.single(User.email == email)
        if user is not None:
            raise JsonException(errcode=1001, errmsg="该邮箱已被注册")
        code = strings.gen_password(6)
        key = self.gen_verify_code_key(email)
        await redis.set(key, code)
        await send_register_code(email, code)
        self.finish_json(result={
        })

    def gen_verify_code_key(self, email):
        return 'email_key_' + strings.md5(email)

