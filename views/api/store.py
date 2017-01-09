# coding=utf-8

from kit.qiniu import get_upload_token

from views import BaseHandler
from models.user import User
from playhouse.shortcuts import model_to_dict, dict_to_model
from exceptions.json import *

class UploadHandler(BaseHandler):

    def get(self):
        filename = self.get_argument("filename")
        token = get_upload_token(filename)
        self.finish_json(result={'token': token})
