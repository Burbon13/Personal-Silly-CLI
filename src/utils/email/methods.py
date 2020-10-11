import requests
from constants import MAIL_GUN_API_KEY, MAIL_GUN_DOMAIN, USER_NAME, MAIL_TEMPLATE_LOCATION, MAIL_REPLY_TO, \
    MAIL_SENDER_NAME, MAIL_BASE_URL


def send_test_email(recipients):
    send_email_with_mailgun(recipients, 'Emailing test :>',
                            'This is an automated email test sent via the CLI silly tool, please ignore it!')


def send_email(recipients, subject, text):
    send_email_with_mailgun(recipients, subject, text)


def send_email_with_mailgun(recipient, subject, text):
    """ Raises Exception if any error occurs """
    with open(MAIL_TEMPLATE_LOCATION, 'r') as file:
        email_html = file.read() \
            .replace('\n', '') \
            .replace('<$greeting$>', subject) \
            .replace('<$text$>', text) \
            .replace('<$sender-name$>', MAIL_SENDER_NAME) \
            .replace('<$reply-to$>', MAIL_REPLY_TO)
        response = requests.post(
            F"{MAIL_BASE_URL}/{MAIL_GUN_DOMAIN}/messages",
            auth=("api", MAIL_GUN_API_KEY),
            data={"from": f"{USER_NAME} <{MAIL_REPLY_TO}>",
                  "to": [recipient],
                  "subject": subject,
                  "html": email_html})

    if response.status_code != 200:
        print(response.status_code)
        raise Exception(response)
