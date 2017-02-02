# coding: utf-8

import asyncio
import aioredis
from kit.config import config

loop = asyncio.get_event_loop()

redis = loop.run_until_complete(aioredis.create_redis((config['redis']['host'], config['redis']['port']), loop=loop))
