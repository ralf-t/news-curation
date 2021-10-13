"""The app module, containing the app factory function."""

from flask import Flask
from os import environ

from news_curation import (
	commands, 
	config, 
	post, 
	user, 
	topic
	)

from news_curation.extensions import (
	db,
	login_manager,
	bcrypt,
	meld
	)

FLASK_ENV = environ['FLASK_ENV']

def create_app(test_config=None):
	"""App Factory"""
	app = Flask(__name__)

	# apply config if may custom test config + test defaults 
	if not test_config is None:
		app.config.from_object(config.TestingConfig)
		app.config.from_mapping(test_config)
	# use env defaults
	elif environ['FLASK_ENV'] == 'development':
		app.config.from_object(config.DevelopmentConfig)
	elif FLASK_ENV == 'production' or FLASK_ENV == 'seeder':
		app.config.from_object(config.ProductionConfig)

	register_extensions(app)
	register_blueprints(app)
	register_commands(app)

	return app

def register_extensions(app):
	db.init_app(app)
	login_manager.init_app(app)
	bcrypt.init_app(app)
	meld.init_app(app)
	return None

def register_blueprints(app):
	app.register_blueprint(user.bp, url_prefix="/user")
	app.register_blueprint(post.bp, url_prefix="/post")
	app.register_blueprint(topic.bp, url_prefix="/topic")
	return None

def register_commands(app):
	app.cli.add_command(commands.up)
	app.cli.add_command(commands.seeder_cli)
	return None
