import click
from ..utils.pdf import create_daily_pdf

@click.group()
def cli():
    """ PDF generator utils """
    pass

@cli.command()
@click.option('--count', default=5, help='How many jokes you want?')
def do_create_daily_pdf(count: int):
    create_daily_pdf(count)
