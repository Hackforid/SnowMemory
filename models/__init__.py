# -*- coding: utf-8 -*-

import peewee
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PooledMySQLDatabase('snowmemory', user="root",
        max_connections=8, stale_timeout=300,)
db.connect()

class BaseModel(peewee.Model):

    def to_dict(self):
        return model_to_dict(self)
