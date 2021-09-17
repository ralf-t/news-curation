"""The app module, containing the app factory function."""

from flask import Flask
from os import environ

from news_curation import commands, settings
from news_curation.extensions import (
	db
	)

def create_app(test_config=None):
	"""App Factory"""
	app = Flask(__name__)

	if not test_config is None:
		app.config.from_object(settings.TestingConfig)
		app.config.from_mapping(test_config)
	elif environ['FLASK_ENV'] == 'development':
		app.config.from_object(settings.DevelopmentConfig)
	elif environ['FLASK_ENV'] == 'production':
		app.config.from_object(settings.ProductionConfig)

	register_extensions(app)
	register_blueprints(app)
	register_commands(app)

	return app

def register_extensions(app):
	db.init_app(app)
	return None

def register_blueprints(app):
	return None

def register_commands(app):
	app.cli.add_command(commands.go)
	return None
