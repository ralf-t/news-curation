'''
db
https://flask.palletsprojects.com/en/2.0.x/tutorial/database/

db setup teardown
https://stackoverflow.com/questions/56063458/pre-populate-a-flask-sqlalchemy-database
https://stackoverflow.com/questions/66876181/how-do-i-close-a-flask-sqlalchemy-connection-that-i-used-in-a-thread
https://stackoverflow.com/questions/14060321/using-pythons-unit-testing-setup-teardown-with-flask-sql-alchemy
https://flask.palletsprojects.com/en/2.0.x/patterns/sqlalchemy/

fixtures, environment with known parameters, or content
https://docs.pytest.org/en/latest/explanation/fixtures.html

pytest run ==> use python -m pytest
https://docs.pytest.org/en/latest/explanation/goodpractices.html#choosing-a-test-layout-import-rules

webtest > flask test client
https://codeinthehole.com/tips/prefer-webtest-to-djangos-test-client-for-functional-tests/
https://docs.pylonsproject.org/projects/webtest/en/latest/
'''
import pytest
import logging

from news_curation import create_app
from webtest import TestApp
from news_curation.database import db as _db

from .factories import UserFactory

@pytest.fixture
def app():
	"""Create application for the tests"""
	_app = create_app({'TESTING': True})
	_app.logger.setLevel(logging.CRITICAL)
	ctx = _app.test_request_context()
	ctx.push()

	yield _app

	ctx.pop()

@pytest.fixture
def testapp(app):
	"""Create Webtest app"""
	return TestApp(app)

@pytest.fixture
def db(app):
	"""Create database for the tests"""
	_db.app = app
	with app.app_context():
		_db.create_all()

	yield _db

	# Explicitly close DB connection
	_db.session.close()
	_db.drop_all()


# TODO
@pytest.fixture
def user(db):
	"""Create user for tests"""
	user = UserFactory(password="osmanthus!wine")
	db.session.commit()
	return user
