#### TODO
- Login & Home modules
	- Navbar active state stuck @ home
	- Macro cleaning
	- Routes homepage filter --> reduce code
	- Forgot password empty page
- Changes (for collab)
	- [ask SD if design good] LOGIN P: added remember & forgot password options


#### SETUP
1. Make a copy of the file `.env.example`, rename it to `.env`, and set environment variables. Or don't change content of file to use default values for development. See `.env.example` file for reference
2. Within cmd, activate virtual environment using:
	`pipenv shell`
3. Then install project dependencies (extensions/ packages/ libraries) using:
	`pipenv install`
4. Drop existing tables and create new ones using:
	`flask reset-tables`
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


