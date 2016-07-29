from os.path import abspath, basename, dirname, join, normpath
from sys import path

from django.conf import global_settings
# Django settings for coreymaynard project.

DJANGO_ROOT = dirname(abspath(__file__))
SITE_ROOT = dirname(DJANGO_ROOT)
SITE_NAME = basename(DJANGO_ROOT)
path.append(DJANGO_ROOT)
path.append(DJANGO_ROOT + '/apps')

MEDIA_ROOT = normpath(join(SITE_ROOT, 'files'))
MEDIA_URL = '/files/'

STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))
STATIC_URL = '/static/'

WSGI_APPLICATION = 'wsgi.application'

CACHE_BACKEND = 'locmem://?timeout=600&max_entires=100'

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

ALLOWED_HOSTS = '*'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'nlz-#l7of9rd5n54sc00+rn3lb@&d#0g)_a_z=izyy_wlcko^e'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'apps.core.context_processors.recent_posts',
    'apps.core.context_processors.is_production',
    'apps.core.context_processors.categories',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    SITE_ROOT +'/templates',
)

STATICFILES_DIRS = global_settings.STATICFILES_DIRS + (
    SITE_ROOT,
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.messages',

    'apps.core',
    'apps.blog',
    'apps.portfolio',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
