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
    """
    Checks if a contact already exists with its name.

    :param contact: the contact to be checked
    :param db:      db reference for TinyDb
    :raises: Exception if another contact already exists
    """
    User = Query()
    existing_contact = db.search((User.name == contact['name']) & (User.surname == contact['surname']))
    if len(existing_contact) > 0:
        raise Exception(f'Contact {contact["name"]} {contact["surname"]} already exists')


def insert_contact(name, surname, email_address, phone, relation):
    """
    Inserts a new contact in the local storage. Name and surname combination must be unique!

    :param name:            the name of the contact (e.g. John)
    :param surname:         the surname of the contact (e.g. Smith)
    :param email_address:   the email of the contact (e.g. john.smith@example.com)
    :param phone:           the phone of the contact (e.g 0770561512)
    :param relation:        family, love, me, friend, other (one of those)
    :raises: Exception of the contact is invalid or if the contact already exists
    """
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
    print('Contact added!')


def delete_contact(name, surname):
    """ Deletes a contact from the local storage """
    User = Query()
    db = TinyDB(TINY_DB_LOCATION)
    db.remove((User.name == name) & (User.surname == surname))


def update_contact(name, surname, email_address, phone, relation):
    """ Updates a contact. Raises exception if no contact is found """
    pass


def get_contacts(criterion_list=None):
    """
    Retrieves the contacts based on some selection criterion.

    :param criterion_list:      A list of criterion for the selection
    :return:                    The list with the selected contacts
    """
    return filter_contacts(TinyDB(TINY_DB_LOCATION).all(), criterion_list)


def filter_contacts(contact_list, criterion_list):
    """
    Filters the contacts based on some selection criterion.

    :param contact_list:        The list of contacts to be filtered
    :param criterion_list:      A list of criterion for the selection. If None, all contacts are returned.
    :return:                    The list with the filtered contacts
    """
    if criterion_list is None:
        return contact_list
    remaining_contacts = []
    for contact in contact_list:
        valid = True
        for criterion in criterion_list:
            if not criterion[1](contact[criterion[0]]):
                valid = False
                break
        if valid:
            remaining_contacts.append(contact)
    return remaining_contacts
