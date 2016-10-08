import os
import redis

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis_conn = redis.from_url(redis_url)


# Add data from lookup table
def add_data():
    # Data lookup table
    pia = {
        'katey bday': 'September 3',
        'carol bday': 'January 12',
        'dan bday': 'July 21',
        'anniv': 'August 17 (2012)',
        'lentil soup': 'lentils, celery, onions, carrots, broth, tomato paste, red wine, thyme, salt, pepper',
        'cornerstone': '031207830',
        'shows': 'black mirror',
        'spinach': 'Trigon commercial: https://www.youtube.com/watch?v=a189xAYBRv8',
        'katey xmas': 'will and grace',
        'simple': '(6x8)11-7(5x2)9-71(19x2)-00(15x2)-m19-5three5',
        'license': 'S3442 40786 04812, exp 4-30-18'
    }
    for key, value in pia.items():
        redis_conn.set(key, value)


if __name__ == "__main__":
    add_data()
