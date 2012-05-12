'''Local settings file, modify to fit your server'''

DEBUG = True
PRODUCTION = False

TEMPLATE_DEBUG = True
TEMPLATE_STRING_IF_INVALID = 'NOT FOUND:%s'

ADMIN_MEDIA_PREFIX = ''
MEDIA_URL = ''

USER_NAME = ''
NAME      = ''
EMAIL     = ''

ADMINS = (
    (NAME, EMAIL),
)
MANAGERS = ADMINS

EMAIL_HOST = ""
EMAIL_PORT = ""

DATABASES = {
    'default': {
        'ENGINE' : '',
        'NAME' : '',
        'USER' : '',
        'PASSWORD' : '',
        'HOST' : '',
        'PORT': '',
        }
}
