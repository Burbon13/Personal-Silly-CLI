import requests
from constants import MAIL_GUN_API_KEY, MAIL_GUN_DOMAIN, USER_NAME, MAIL_TEMPLATE_LOCATION, MAIL_REPLY_TO, \
    MAIL_SENDER_NAME, MAIL_BASE_URL


def send_test_email(recipients):
    """
    Sends a test email.

    :param recipients:  The recipient email address
    """
    send_email_with_mailgun(recipients, 'Emailing test :>',
                            'This is an automated email test sent via the CLI silly tool, please ignore it!')


def send_email(recipient, subject, text, attached_files=None, image=None):
    """
    Sends an email to one recipient.

    :param image:
    :param attached_files:
    :param recipient:   The recipient email address
    :param subject:     The subject of the email
    :param text:        The message to be sent
    """
    if attached_files is None:
        attached_files = []
    send_email_with_mailgun(recipient, subject, text, attached_files, image)


def send_email_with_mailgun(recipient, subject, text, attached_files=None, image=None):
    """
    Sends email to one user via the Mailgun API

    :param image:
    :param attached_files:
    :param recipient:   The recipient email address
    :param subject:     The subject of the email
    :param text:        The message to be sent
    """
    if attached_files is None:
        attached_files = []
    with open(MAIL_TEMPLATE_LOCATION, 'r') as file:
        image_html = '' if image is None else f'<img width="400vw" src="cid:{image["name"]}">'
        files = [("attachment", attached) for attached in attached_files]
        if image is not None:
            files.append(("inline", image["attached"]))
            email_html = file.read() \
                .replace('\n', '') \
                .replace('<$greeting$>', subject) \
                .replace('<$text$>', text) \
                .replace('<$sender-name$>', MAIL_SENDER_NAME) \
                .replace('<$reply-to$>', MAIL_REPLY_TO) \
                .replace('<$image$>', image_html)
            response = requests.post(
                F"{MAIL_BASE_URL}/{MAIL_GUN_DOMAIN}/messages",
                auth=("api", MAIL_GUN_API_KEY),
                files=files,
                data={"from": f"{USER_NAME} <{MAIL_REPLY_TO}>",
                      "to": [recipient],
                      "subject": subject,
                      "html": email_html})

            if response.status_code != 200:
                print('Error occurred:', response.status_code)
