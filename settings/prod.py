'''Production settings file'''
import os
import dj_database_url
from .common import *

DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
PRODUCTION = True

SECRET_KEY = os.environ.get('SECRET_KEY', "")

ALLOWED_HOSTS = [
    os.environ.get("CUSTOM_DOMAIN", "coreymaynard.com"),
    os.environ.get('RENDER_EXTERNAL_HOSTNAME', '')
]

USER_NAME = 'cjmaynar'
NAME = 'Corey Maynard'
EMAIL = 'me@coreymayard.com'

ADMINS = (
    (NAME, EMAIL),
)
MANAGERS = ADMINS

EMAIL_HOST = ""
EMAIL_PORT = ""

# WhiteNoise for static file serving
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
] + MIDDLEWARE[1:]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# PostgreSQL via DATABASE_URL env var
DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    )
}
