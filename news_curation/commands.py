"""Command line interface for development shortcuts"""

# TODO: setup config values related to env
# TODO: setuptools https://click.palletsprojects.com/en/8.0.x/setuptools/#setuptools-integration
# TODO (copy @ test py files) https://flask.palletsprojects.com/en/2.0.x/testing/#testing-cli

from flask.cli import with_appcontext
from os import environ, system
import click

@click.command('go')
@click.argument('flask_env', default='dev')
@with_appcontext
def go(flask_env):
	"""Run flask app within the specified environment. flask go prod; flask go dev"""
	environ['FLASK_ENV'] = 'development' if flask_env == 'dev' else 'development'
	environ['FLASK_ENV'] = 'production' if flask_env == 'prod' else 'development'
	system('flask run')	