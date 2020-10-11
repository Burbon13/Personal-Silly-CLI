import click
from ..utils import send_email, send_test_email


@click.group()
def cli():
    """ Communication commands """
    pass


@cli.command()
@click.option('--to', help='To whom you want to send the email')
def email_test(to):
    """ Send a test email """
    send_test_email(to)


@cli.command()
@click.option('--to', help='To whom you want to send the email')
@click.option('--subject', help='The subject of the email')
@click.option('--text', help='The text of the email')
def email(to, subject, text):
    """ Send an email """
    send_email(to, subject, text)


if __name__ == '__main__':
    cli()
