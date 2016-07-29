from .common import *

DEBUG = True
PRODUCTION = False

TEMPLATE_DEBUG = True
TEMPLATE_STRING_IF_INVALID = 'NOT FOUND:%s'

USER_NAME = 'cjmaynar'
NAME = 'Corey Maynard'
EMAIL = 'me@coreymayard.com'

ADMINS = (
    (NAME, EMAIL),
)
MANAGERS = ADMINS

EMAIL_HOST = ""
EMAIL_PORT = ""

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'devSecretKey'

# Use sqlite3 for development database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'coreymaynard.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
}
