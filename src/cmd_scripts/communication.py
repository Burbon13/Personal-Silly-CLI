import click
from ..utils import send_email


@click.group()
def cli():
    """ Communication commands """
    pass


@cli.command()
@click.option('--recipients', help='To whom you want to send the email')
@click.option('--subject', help='The subject of the email')
@click.option('--text', help='The text of the email')
def email(recipients, subject, text):
    """ Send an email """
    send_email(recipients, subject, text)


if __name__ == '__main__':
    cli()
