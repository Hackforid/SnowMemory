# -*- coding: utf-8 -*-

import peewee
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import model_to_dict, dict_to_model
from utils.json import json_encode, json_decode
from kit.config import config

sql_config = config['mysql']

db = PooledMySQLDatabase('snowmemory', user=sql_config['user'],
        password=sql_config.get('password', ''),
        host=sql_config['host'],
        max_connections=8, stale_timeout=300,)
db.connect()

class BaseModel(peewee.Model):

    def to_dict(self):
        return model_to_dict(self)

    @classmethod
    def single(cls, *args):
        result = None
        try:
            result = cls.get(*args)
        except Exception as e:
            print(e)
        return result

    class Meta:
        database = db

