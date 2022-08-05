import click
import pyperclip


# https://click.palletsprojects.com/en/8.1.x/api/#click.version_option
@click.command()
@click.version_option()
def run():
    """Generate a list of installation commands for a package to add to README files."""
    click.echo("Hello, World!")
