import click
from ..utils.cli import make_selection_in_cli
from ..data.contacts import insert_contact, get_contacts, delete_contact as delete_contact_data
from ..utils.contacts import contact_to_string
from ..utils.email import send_test_email, send_email
from ..utils.sms import send_test_sms, send_sms


@click.group()
def cli():
    """ Communication commands """
    pass


@cli.command()
@click.argument('name')
@click.argument('surname')
def delete_contact(name, surname):
    """ Deletes a contact from the local storage """
    delete_contact_data(name, surname)


@cli.command()
def my_contacts():
    """ Prints all saved contacts """
    contact_list = get_contacts()
    if len(contact_list) == 0:
        click.echo(click.style('You have no contacts :(', fg='bright_yellow'))
    for contact in contact_list:
        click.echo(contact_to_string(contact))


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
        click.echo(click.style(f'Contact error: {e}', fg='red'))


@cli.command()
@click.option('--to', help='To whom you want to send the SMS (phone number)')
def sms_test(to):
    """ Send a test SMS """
    send_test_sms(to)


@cli.command()
@click.option('--to', help='To whom you want to send the SMS (phone number)')
@click.option('--relation', help='The relation with the person',
              type=click.Choice(['family', 'love', 'friend', 'me', 'other'], case_sensitive=False))
@click.option('--name', help='First name')
@click.argument('text')
def sms(to, relation, name, text):
    """ Send an SMS to ONE person """
    contacts_list = get_contacts([
        ('phone', lambda x: True if to is None else x == to),
        ('relation', lambda x: True if relation is None else x == relation),
        ('name', lambda x: True if name is None else x.lower().startswith(name.lower())),
    ])
    contact = make_selection_in_cli(contacts_list, contact_to_string, click)
    if contact is not None:
        send_sms(contact['phone'], text)
    else:
        click.echo(click.style('No contact found :(', fg='bright_yellow'))


@cli.command()
@click.option('--to', help='To whom you want to send the email')
def email_test(to):
    """ Send a test email """
    send_test_email(to)


@cli.command()
@click.option('--to', help='To whom you want to send the email')
@click.option('--subject', help='The subject of the email')
@click.option('--text', help='The text of the email')
@click.option('--attachment', help='File to be added to the email')
def email(to, subject, text, attachment):
    """ Send an email """
    if attachment is None:
        send_email(to, subject, text)
    else:
        try:
            with open(attachment, 'rb') as in_file:
                send_email(to, subject, text, [in_file])
        except Exception as e:
            click.echo(click.style(f'Error occurred: {e}', fg='red'))


if __name__ == '__main__':
    cli()
