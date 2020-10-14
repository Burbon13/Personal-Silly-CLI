def contact_to_string(contact) -> str:
    """
    Converts a contact to a pretty formatted string.

    :param contact:  Dict, must contain:
                        - name
                        - surname
                        - relation
                        - phone
                        - email_address
    :returns The formatted string
    """
    return f'{contact["name"]} {contact["surname"]} ({contact["relation"]}):  {contact["phone"]}' \
           + f'  {contact["email_address"]}'
