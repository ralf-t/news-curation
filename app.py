# https://flask.palletsprojects.com/en/2.0.x/quickstart/

# As a shortcut, if the file is named app.py or wsgi.py, 
# you don’t have to set the FLASK_APP environment variable.

from news_curation import create_app
from os import environ

app = create_app()

if environ.get('FLASK_ENV') == "seeder":
    pass
elif __name__ == '__main__':
    app.run()

