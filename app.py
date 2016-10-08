import os
import redis

from flask import Flask, render_template, request

app = Flask(__name__)
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis_conn = redis.from_url(redis_url)


def redis_get(redis, key):
    value = redis.get(key)
    if value:
        value = value.decode('ascii')
    return value


@app.route('/', methods=['GET', 'POST'])
def home():
    key = ''
    search_result = ''
    add_result = ''
    if request.method == 'POST':
        # Get the user's inputs from the form
        query = request.form.get('query', '')
        key = request.form.get('key', '')
        value = request.form.get('value', '')
        if key and value:
            existing_value = redis_get(redis_conn, key)
            print(existing_value)
            if existing_value:
                add_result = 'The key "{}" is already stored, with value: "{}"'.format(
                    key, existing_value)
            else:
                redis_conn.set(key, value)
                add_result = 'The key "{}" has been stored with value: "{}"'.format(key, value)
                key = ''
        else:
            # Look for user query in redis
            search_result = redis_get(redis_conn, query)
            # If not found, return a message indicating no search_results
            if not search_result:
                search_result = 'No results found'
                key = query
    return render_template('home.html', key=key, search_result=search_result, add_result=add_result)


if __name__ == "__main__":
    app.run()
