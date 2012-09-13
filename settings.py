import os, sys
from django.conf import global_settings
# Django settings for coreymaynard project.

PROJECT_ROOT = os.path.dirname(__file__)
MEDIA_ROOT = PROJECT_ROOT+'/files/'

CACHE_BACKEND = 'locmem://?timeout=600&max_entires=100'

# Apps Folder
sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'nlz-#l7of9rd5n54sc00+rn3lb@&d#0g)_a_z=izyy_wlcko^e'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'core.context_processors.grooveshark',
    'core.context_processors.recent_posts',
    'core.context_processors.is_production',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    PROJECT_ROOT+'/templates',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.markup',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'core',
    'blog',
    'portfolio',
)

try:
    from local_settings import *
except ImportError:
    pass
