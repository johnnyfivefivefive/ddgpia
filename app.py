from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    # Data lookup table
    pia = {
        'Hx88Wtn92Ppwgh4 katey bday': 'September 3',
        'Hx88Wtn92Ppwgh4 carol bday': 'January 12',
        'Hx88Wtn92Ppwgh4 dan bday': 'July 21',
        'Hx88Wtn92Ppwgh4 anniv': 'August 17 (2012)',
        'Hx88Wtn92Ppwgh4 lentil soup': 'lentils, celery, onions, carrots, broth, tomato paste, red wine, thyme, salt, pepper',
        'Hx88Wtn92Ppwgh4 cornerstone': '031207830',
        'Hx88Wtn92Ppwgh4 shows': 'black mirror',
        'Hx88Wtn92Ppwgh4 spinach': 'Trigon commercial: https://www.youtube.com/watch?v=a189xAYBRv8',
        'hx88wtn92ppwgh4 katey bday': 'September 3',
        'hx88wtn92ppwgh4 carol bday': 'January 12',
        'hx88wtn92ppwgh4 dan bday': 'July 21',
        'hx88wtn92ppwgh4 anniv': 'August 17 (2012)',
        'hx88wtn92ppwgh4 lentil soup': 'lentils, celery, onions, carrots, broth, tomato paste, red wine, thyme, salt, pepper',
        'hx88Wtn92Ppwgh4 cornerstone': '031207830',
        'hx88wtn92ppwgh4 shows': 'black mirror',
        'hx88wtn92ppwgh4 spinach': 'Trigon commercial: https://www.youtube.com/watch?v=a189xAYBRv8',
    }
    result = ''
    if request.method == 'POST':
        # Get the user's query from the form
        query = request.form.get('query')
        # Try to get a lookup for the user query; if not found, result a message indicated no results
        result = pia.get(query, 'No results found')
    return render_template('home.html', result=result)
