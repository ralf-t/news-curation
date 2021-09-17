# https://flask.palletsprojects.com/en/2.0.x/quickstart/

# As a shortcut, if the file is named app.py or wsgi.py, 
# you don’t have to set the FLASK_APP environment variable.

from news_curation import create_app

app = create_app()

if __name__ == '__main__':
    app.run()

