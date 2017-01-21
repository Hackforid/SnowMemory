# coding: utf-8

import asyncio
import aioredis

loop = asyncio.get_event_loop()

redis = loop.run_until_complete(aioredis.create_redis(('localhost', 6379), loop=loop))
