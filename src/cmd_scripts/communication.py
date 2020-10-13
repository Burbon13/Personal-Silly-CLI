import click
from ..utils import send_email, send_test_email, send_test_sms, send_sms, insert_contact, get_contacts


@click.group()
def cli():
    """ Communication commands """
    pass


@cli.command()
def print_contacts():
    """ Prints all saved contacts """
    contact_list = get_contacts()
    if len(contact_list) == 0:
        print('You have no contacts :(')
    for contact in contact_list:
        print(contact)


@cli.command()
@click.argument('name')
@click.argument('surname')
@click.argument('email_address')
@click.argument('phone')
@click.argument('relation')
def create_contact(name, surname, email_address, phone, relation):
    """ Create and store a contact locally """
    try:
        insert_contact(name, surname, email_address, phone, relation)
    except Exception as e:
        print('Contact error:', str(e))


@cli.command()
@click.option('--to', help='To whom you want to send the SMS (phone number)')
def sms_test(to):
    """ Send a test SMS """
    send_test_sms(to)


@cli.command()
@click.option('--to', help='To whom you want to send the SMS (phone number)')
@click.option('--text', help='The text of the email')
def sms(to, text):
    """ Send an SMS """
    send_sms(to, text)


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
