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
    'import_export',
]

LOCAL_APPS = [
    'apps.blog',
    'apps.diary',
    'apps.files',
    'apps.main',
    'apps.music',
    'apps.news',
    'apps.users',
]

INSTALLED_APPS += LOCAL_APPS
