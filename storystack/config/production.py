# Settings that are unique to production go here
import django_heroku
from .base import *  # noqa
import os
DEBUG = False

# Configure Django App for Heroku.
django_heroku.settings(locals())
# # Anymail (Mailgun)
# # ------------------------------------------------------------------------------
# # https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
# INSTALLED_APPS += ['anymail']
EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
# https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
ANYMAIL = {
    'MAILGUN_API_KEY': os.environ.get('MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': os.environ.get('MAILGUN_DOMAIN')
}

MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
MAILGUN_SENDER_DOMAIN = os.environ.get('MAILGUN_DOMAIN')


EMAIL_HOST = MAILGUN_SENDER_DOMAIN
EMAIL_PORT = 587
# EMAIL_HOST_USER = 'testsite_app'
# EMAIL_HOST_PASSWORD = 'mys3cr3tp4ssw0rd'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'user@storystack.com'
