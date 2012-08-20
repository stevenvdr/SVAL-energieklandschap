# -*- coding: utf-8 -*-
# This settings file should contain all settings that are specific for development
# servers
# Beware not to put any sensitive information in this file!
import os

from base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'mycms.db'),
        }
}

