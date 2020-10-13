from tinydb import TinyDB, Query
from constants import TINY_DB_LOCATION
from ..sms import is_valid_number
from validate_email import validate_email

REQUIRED_CONTACT_ATTRIBUTES = [
    (
        'name',
        lambda x: x is not None and len(x) > 3,
        'Name must have at least 3 characters'
    ),
    (
        'surname',
        lambda x: x is not None and len(x) > 3,
        'Surname must have at least 3 characters'
    ),
    (
        'phone',
        lambda x: is_valid_number(x),
        'Phone number is invalid'
    ),
    (
        'email_address',
        lambda x: validate_email(x),
        'Email address must be valid'
    ),
    (
        'relation',
        lambda x: x in ['family', 'love', 'friend', 'me', 'other'],
        'Relation can only be one of the following: family, love, friend, me or other'
    )
]


def verify_contact(contact):
    """
    Check if a contact is valid. A contact is valid if it contains the following characteristics:
    - name (at least 4 characters)
    - surname (at least 4 characters)
    - phone (must be valid)
    - email (must be valid)
    - relation (must be family, love, friend or other)

    :param contact: the object to be verified
    :raises: Exception if contact is not valid
    """
    for characteristic in REQUIRED_CONTACT_ATTRIBUTES:
        if characteristic[0] not in contact:
            raise Exception(f'Contact does not have {characteristic[0]}')
        if not characteristic[1](contact[characteristic[0]]):
            raise Exception(characteristic[2])


def is_contact_unique(contact, db):
    """ TODO """
    return True


def insert_contact(name, surname, email_address, phone, relation):
    contact = {
        'name': name,
        'surname': surname,
        'email_address': email_address,
        'phone': phone,
        'relation': relation
    }
    verify_contact(contact)
    db = TinyDB(TINY_DB_LOCATION)
    is_contact_unique(contact, db)
    db.insert(contact)


def get_contacts():
    db = TinyDB(TINY_DB_LOCATION)
    return db.all()
