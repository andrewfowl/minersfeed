import os
import redis
from urllib.parse import urlparse

redis_url = os.getenv('REDIS_URL', 'localhost')
parsed_url = urlparse(redis_url)

REDIS_HOST = os.getenv('REDISHOST', parsed_url.hostname)
REDIS_PORT = os.getenv('REDISPORT', parsed_url.port)
REDIS_PASSWORD = os.getenv('REDISPASSWORD', parsed_url.password)
