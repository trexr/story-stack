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
