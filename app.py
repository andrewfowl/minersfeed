from flask import Flask, jsonify
from rss_feed_service_redis import get_combined_feed

app = Flask(__name__)

@app.route('/api/feed', methods=['GET'])
def get_feed():
    feed_items = get_combined_feed()
    return jsonify(feed_items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
