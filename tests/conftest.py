'''
REFS

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

@pytest.fixture
def app():
	pass

@pytest.fixture
def testapp(app):
	pass

@pytest.fixture
def db(app):
	pass

@pytest.fixture
def user(db):
	pass
