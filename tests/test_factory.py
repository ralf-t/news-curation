"""SOFTWARE TESTER. Test application factory and route responses"""

'''
test cases
https://flask.palletsprojects.com/en/2.0.x/testing/
https://flask.palletsprojects.com/en/2.0.x/tutorial/tests/
https://flask.palletsprojects.com/en/2.0.x/testing/#testing-cli
'''

from news_curation import create_app

def test_config():
	assert not create_app().testing
	assert create_app({'TESTING': True}).testing
