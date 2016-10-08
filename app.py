import os
import redis

from flask import Flask, render_template, request

app = Flask(__name__)
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis_conn = redis.from_url(redis_url)


@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''
    if request.method == 'POST':
        # Get the user's query from the form
        query = request.form.get('query')
        # Look for user query in redis
        result = redis_conn.get(query)
        # If not found, return a message indicating no results
        if not result:
            result = 'No results found'
    return render_template('home.html', result=result)


if __name__ == "__main__":
    app.run()
