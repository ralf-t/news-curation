#### ST: DOING
- [Flask-Meld](https://docs.flask-meld.dev/components/) 
	- [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/getting_started.html)
	- [Real-time form validation](https://www.reddit.com/r/flask/comments/p2obob/realtime_form_validation_with_flaskmeld_no/)
	- [Custom attributes for Flask WTForms](https://stackoverflow.com/questions/20440056/custom-attributes-for-flask-wtforms/27118147)
	- [Instagram form field reference](https://www.instagram.com/)
	- [Flask Meld Templates](https://docs.flask-meld.dev/templates/)


- problems: cannot do lazy validation
			still cant make flask flash work with meld component
			render_kw does not work after melding

- continue: [fork a package & customize](https://stackoverflow.com/questions/23075397/python-how-to-edit-an-installed-package)
		  : [flask meld package source](https://github.com/mikeabrahamsen/Flask-Meld/blob/main/flask_meld/component.py)
		  
#### TODO
- Login & Home modules
	- Macro cleaning
	- Routes homepage filter --> reduce code
- Registration for firstname, lastname does not work for the ff input:
	- T'challa
	- O'brien
	- J'onn

<!-- **{"placeholder":placeholder} -->
<!-- placeholder=placeholder -->


#### SETUP
1. Make a copy of the file `.env.example`, rename it to `.env`, and set environment variables. Or don't change content of file to use default values for development. See `.env.example` file for reference
2. Within cmd, activate virtual environment using:
	`pipenv shell`
3. Then install project dependencies (extensions/ packages/ libraries) using:
	`pipenv install`
4. Reset database (the db specified at .env file) and populate with dummy data using:
	`flask seeder setup`
5. Run the app (must be inside virtual env) using:
	`flask run`
* Alternatively, run app in development using:
	`flask up dev`
* Run app in production using:
	`flask up prod`




#### DEVELOPMENT/ EXPLORE 
1. Display available URLs using:
	`flask routes`
2. Test application after changes are made using:
	`pytest`
3. Reset database (the db specified at .env file) and populate with dummy data using:
	`flask seeder setup`
4. Drop tables using:
	`flask seeder teardown`


