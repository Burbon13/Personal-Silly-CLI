def contact_to_string(contact):
    """

    :param contact:
    :return:
    """
    return f'{contact["name"]} {contact["surname"]} ({contact["relation"]}):  {contact["phone"]}' \
           + f'  {contact["email_address"]}'
