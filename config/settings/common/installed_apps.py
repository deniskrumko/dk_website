INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'adminsortable',
    'django_object_actions',
    'imagekit',
]

LOCAL_APPS = [
    'apps.users',
    'apps.music',
    'apps.files',
]

INSTALLED_APPS += LOCAL_APPS
