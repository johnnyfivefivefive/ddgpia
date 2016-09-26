from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
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
    result = ''
    if request.method == 'POST':
        # Get the user's query from the form
        query = request.form.get('query')
        # Try to get a lookup for the user query; if not found, result a message indicated no results
        result = pia.get(query, 'No results found')
    return render_template('home.html', result=result)
