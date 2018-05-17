from .common import *  # noqa

import dj_database_url


SECRET_KEY = 'example'

DEBUG = True

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:@localhost:5432/deniskrumko'
    )
}

AUTH_PASSWORD_VALIDATORS = []

# DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Shell plus pre imports
SHELL_PLUS_PRE_IMPORTS = [('{}.factories'.format(app), '*')
                          for app in INSTALLED_APPS]  # noqa

WEBSITE_URL = 'http://127.0.0.1:8000/'
