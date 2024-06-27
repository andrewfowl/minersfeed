import feedparser
import redis
import logging
from datetime import datetime
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD
from urls import feed_urls

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_feed(feed_url):
    try:
        return feedparser.parse(feed_url)
    except Exception as e:
        logging.error(f"Failed to fetch feed {feed_url}: {e}")
        return None

def store_feed_items(feed, redis_client):
    if feed is None:
        return

    for entry in feed.entries:
        if not redis_client.sismember('rss_links', entry.link):
            try:
                rss_item = {
                    'title': entry.get('title', 'No title'),
                    'link': entry.get('link', 'No link'),
                    'published': datetime(*entry.published_parsed[:6]).isoformat() if entry.get('published_parsed') else 'No date',
                    'summary': entry.get('summary', 'No summary')
                }
                redis_client.sadd('rss_links', entry.link)
                redis_client.hmset(f"rss_item:{entry.link}", rss_item)
            except Exception as e:
                logging.error(f"Failed to store feed item {entry.link}: {e}")

def main():
    redis_client = redis.StrictRedis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        password=REDIS_PASSWORD,
        decode_responses=True
    )
    for url in feed_urls:
        feed = fetch_feed(url)
        store_feed_items(feed, redis_client)

def get_combined_feed():
    redis_client = redis.StrictRedis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        password=REDIS_PASSWORD,
        decode_responses=True
    )
    keys = redis_client.smembers('rss_links')
    feed_items = [redis_client.hgetall(f"rss_item:{key}") for key in keys]
    return feed_items

if __name__ == "__main__":
    main()
