import schedule
import time
from rss_feed_service_redis import main

def job():
    main()

schedule.every(180).minutes.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
