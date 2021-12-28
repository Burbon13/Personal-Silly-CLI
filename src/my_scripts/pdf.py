import click
from ..utils.pdf import create_daily_pdf

@click.group()
def cli():
    """ News aggregator from several APIs/Websites """
    pass

@cli.command()
def do_create_daily_pdf():
    create_daily_pdf()
