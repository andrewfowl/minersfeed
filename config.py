import os
import redis
from urllib.parse import urlparse

redis_url = os.getenv('REDIS_URL', 'localhost')
parsed_url = urlparse(redis_url)

REDIS_HOST = os.getenv('REDISHOST', 'localhost')
REDIS_PORT = os.getenv('REDISPORT', 6379)
REDIS_PASSWORD = os.getenv('REDISPASSWORD', None)
