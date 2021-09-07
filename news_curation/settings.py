"""
Most configuration is set via environment variables, see .env or .env.example file

For local development,
use a .env file to set environment variables;
rename .env.example file to .env and set the variables applicable to your development environment

Reference
https://flask.palletsprojects.com/en/2.0.x/config/#development-production
"""

from os import environ
import secrets

class Config(object):
	ENV = environ.get('FLASK_ENV', default="production")
	DEBUG = ENV == "development"
	SECRET_KEY = 'dev'
	TESTING = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI', default="sqlite:///:memory:")


class DevelopmentConfig(Config):
	pass


class ProductionConfig(Config):
	SECRET_KEY = secrets.token_hex(24)
	pass


class TestingConfig(Config):
	SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
	TESTING = True