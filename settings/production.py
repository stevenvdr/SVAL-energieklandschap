# -*- coding: utf-8 -*-
# This settings file should contain all settings that are specific for production
# servers
# Beware not to put any sensitive information in this file!

from base import *

DEBUG = False

INSTALLED_APPS += (
    'reversion',
)

TEMPLATE_LOADERS = (
   ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
   )),
)

# Override the server-derived value of SCRIPT_NAME
# See http://code.djangoproject.com/wiki/BackwardsIncompatibleChanges#lighttpdfastcgiandothers
FORCE_SCRIPT_NAME = ''

# Add database information to local settings file