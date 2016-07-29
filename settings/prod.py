'''Production settings file'''
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

# Source the secret key
try:
    from secret import SECRET_KEY
except ImportError:
    SECRET_KEY = None

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
}
