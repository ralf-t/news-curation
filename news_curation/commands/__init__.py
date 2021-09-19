"""Command line interface for development shortcuts"""

# TODO: setup config values related to env
#       setuptools https://click.palletsprojects.com/en/8.0.x/setuptools/#setuptools-integration
#       (copy @ test py files) https://flask.palletsprojects.com/en/2.0.x/testing/#testing-cli

from flask.cli import with_appcontext, AppGroup
from os import environ, system
import click

# appgroup CLIs
seeder_cli = AppGroup("seeder")

# not using @app.cli to avoid doing create_app here lol

@click.command('up')
@click.argument('flask_env')
@with_appcontext
def up(flask_env):
	"""Run flask app within the specified environment. flask up prod; flask up dev"""
	environ['FLASK_ENV'] = 'production' if flask_env == 'prod' else 'development'
	system('flask run')	

from news_curation.commands import seeder