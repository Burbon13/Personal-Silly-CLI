from twilio.rest import Client
from constants import SILLY_CLI_TWILIO_ACCOUNT_SID, SILLY_CLI_TWILIO_AUTH_TOKEN, SILLY_CLI_TWILIO_MY_PHONE_NUMBER


def send_sms(recipients, text):
    send_sms_with_twilio(recipients, text)


def send_test_sms(recipients):
    send_sms_with_twilio(recipients,
                         'This is an automated sms test sent via the CLI silly tool, please ignore it!\n'
                         + 'Best, Razvan Roatis')


def send_sms_with_twilio(recipient, text):
    client = Client(SILLY_CLI_TWILIO_ACCOUNT_SID, SILLY_CLI_TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=text,
        from_=SILLY_CLI_TWILIO_MY_PHONE_NUMBER,
        to=recipient
    )
    print('SMS ID', message.sid)
