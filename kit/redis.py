# coding: utf-8

import asyncio
import aioredis

redis = None

def init(loop):
    global redis
    redis = loop.run_until_complete(aioredis.create_redis(
        ('localhost', 6379), loop=loop))

def db():
    return redis
