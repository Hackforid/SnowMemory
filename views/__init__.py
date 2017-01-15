# -*- coding: utf-8 -*-

import traceback

from tornado.web import RequestHandler
from models import db
from tornado.escape import json_encode, json_decode
from tornado.util import ObjectDict
from exceptions.json import *
from models.auth import Auth
from models.user import User



class BaseHandler(RequestHandler):

    def options(self):
        self.set_status(204)
        self.finish()

    def prepare(self):
        db.connect()
        return super(BaseHandler, self).prepare()

    def on_finish(self):
        if not db.is_closed():
            db.close()
        return super(BaseHandler, self).on_finish()

    def finish_json(self, errcode=0, errmsg=None, result=None):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        resp_json = json_encode({'errcode': errcode,
                    'errmsg': errmsg,
                                 'result': result})
        self.finish(resp_json)

    def _handle_request_exception(self, e):
        db.rollback()
        if isinstance(e, JsonException):
            print(e.to_json())
            self.finish_json(errcode=e.errcode, errmsg=e.errmsg)
        else:
            super(BaseHandler, self)._handle_request_exception(e)

    def get_json_arguments(self, raise_error=True):
        try:
            return ObjectDict(json_decode(self.request.body))
        except Exception as e:
            print(traceback.format_exc())
            if raise_error:
                raise JsonDecodeError()

    def get_current_user(self):
        username = self.request.headers.get('username', None)
        access_token = self.request.headers.get('access_token', None)
        if username is None or access_token is None:
            return None
        user = User.single(User.username == username)
        if user is None:
            return None
        auth = Auth.single(Auth.source_id == 0 and Auth.user_id == user.id)
        if auth.access_token == access_token:
            return user
        else:
            return None


