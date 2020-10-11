import os

# Your name
USER_NAME = os.environ['SILLY_CLI_USER_NAME']

# https://openweathermap.org/guide
OPEN_WEATHER_API_KEY = os.environ['SILLY_CLI_OPEN_WEATHER_API_KEY']

# https://newsapi.org
NEWS_API_KEY = os.environ['SILLY_CLI_NEWS_API_KEY']

# https://app.mailgun.com
MAIL_GUN_API_KEY = os.environ['SILLY_CLI_MAIL_GUN_API_KEY']
MAIL_GUN_DOMAIN = os.environ['SILLY_CLI_MAIL_GUN_DOMAIN']

MAIL_BASE_URL = 'https://api.eu.mailgun.net/v3'
MAIL_TEMPLATE_LOCATION = os.environ['SILLY_CLI_MAIL_TEMPLATE_LOCATION']
MAIL_REPLY_TO = os.environ['SILLY_CLI_MAIL_REPLY_TO']
MAIL_SENDER_NAME = os.environ['SILLY_CLI_MAIL_SENDER_NAME']

# https://www.twilio.com
SILLY_CLI_TWILIO_ACCOUNT_SID = os.environ['SILLY_CLI_TWILIO_ACCOUNT_SID']
SILLY_CLI_TWILIO_AUTH_TOKEN = os.environ['SILLY_CLI_TWILIO_AUTH_TOKEN']
SILLY_CLI_TWILIO_MY_PHONE_NUMBER = os.environ['SILLY_CLI_TWILIO_MY_PHONE_NUMBER']
