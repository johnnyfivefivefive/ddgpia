pia
======

Lookups

### Setup

Create a virtualenvironment using python3
export FLASK_APP=app.py  # Can add to activate script
Activate virtualenvironment
pip install -r requirements.txt


### Running the app (command line)

workon pia  # Ignore warnings
python -m flask run


### Running the app (PyCharm)

Click the arrow next to the "pia flask" run configuration


### Running the app (gunicorn)

gunicorn app:app  # This is how the app runs on heroku


### Deploying the app

Commit changes in PyCharm
git push heroku master
App is at https://ddgpia.herokuapp.com
