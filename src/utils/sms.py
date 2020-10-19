from twilio.rest import Client
from constants import SILLY_CLI_TWILIO_ACCOUNT_SID, SILLY_CLI_TWILIO_AUTH_TOKEN, SILLY_CLI_TWILIO_MY_PHONE_NUMBER
from twilio.base.exceptions import TwilioRestException


def is_valid_number(number) -> bool:
    """
    Check whether a phone number is valid or not

    :param number: the number to be checked
    :return: True if valid, False otherwise
    """
    try:
        return is_valid_number_twilio(number)
    except TwilioRestException as e:
        print('Error occurred in phone validity check')
        return False


def is_valid_number_twilio(number) -> bool:
    """
    Check whether a phone number is valid or not

    :param number: the number to be checked
    :return: True if valid, False otherwise
    :raises: TwilioRestException if any error occurs
    """
    print(f'Verifying validity of phone number {number} via Twilio')
    client = Client(SILLY_CLI_TWILIO_ACCOUNT_SID, SILLY_CLI_TWILIO_AUTH_TOKEN)
    try:
        client.lookups.phone_numbers(number).fetch(type="carrier")
        return True
    except TwilioRestException as e:
        if e.code == 20404:
            return False
        raise e


def send_sms(recipient, text):
    """
    Sends a sms to the recipient.

    :param recipient:   Valid phone number (add national prefix)
    :param text:        The message to be sent
    """
    send_sms_with_twilio(recipient, text)


def send_test_sms(recipient):
    """
    Sends a test sms.

    :param recipient:   Valid phone number (add national prefix)
    :return:
    """
    send_sms_with_twilio(recipient,
                         'This is an automated sms test sent via the CLI silly tool, please ignore it!\n'
                         + 'Best, Razvan Roatis')


def send_sms_with_twilio(recipient, text):
    """
    Sends a SMS to a given number via the Twilio API

    :param recipient: the recipient phone number
    :param text:      the body of the message
    """
    client = Client(SILLY_CLI_TWILIO_ACCOUNT_SID, SILLY_CLI_TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            body=text,
            from_=SILLY_CLI_TWILIO_MY_PHONE_NUMBER,
            to=recipient
        )
        print(f'Message sent! SID: {message.sid}')
    except TwilioRestException as e:
        print('Error occurred:', e)
