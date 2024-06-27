import os
import redis
from urllib.parse import urlparse

redis_url = os.getenv('REDIS_URL', 'localhost')
parsed_url = urlparse(redis_url)

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)