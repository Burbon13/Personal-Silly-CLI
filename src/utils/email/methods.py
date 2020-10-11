import requests
from constants import MAIL_GUN_API_KEY, MAIL_GUN_DOMAIN, USER_NAME, MAIL_TEMPLATE_LOCATION, MAIL_REPLY_TO, \
    MAIL_SENDER_NAME


def send_test_email(recipients):
    send_email_with_mailgun(recipients, 'Emailing test :>', 'This is an automated email test, please ignore it!')


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
            F"https://api.mailgun.net/v3/{MAIL_GUN_DOMAIN}/messages",
            auth=("api", MAIL_GUN_API_KEY),
            data={"from": f"{USER_NAME} <mailgun@{MAIL_GUN_DOMAIN}>",
                  "to": [recipient],
                  "subject": subject,
                  "html": email_html})

    if response.status_code != 200:
        raise Exception(response.json()['message'])
