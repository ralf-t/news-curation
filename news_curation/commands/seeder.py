"""seeder commands"""

from news_curation.commands import with_appcontext, seeder_cli
import click

# todo
# connect sqlite

@seeder_cli.command("setup")
@with_appcontext
def setUp():
	click.echo("su")

@seeder_cli.command("teardown")
@with_appcontext
def tearDown():
	click.echo("td")