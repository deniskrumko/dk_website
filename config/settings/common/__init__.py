from .auth import *  # noqa
from .aws_s3 import *  # noqa
from .ckeditor import *  # noqa
from .datetime import *  # noqa
from .imagekit import *  # noqa
from .installed_apps import *  # noqa
from .locales import *  # noqa
from .logging import *  # noqa
from .middleware import *  # noqa
from .paths import *  # noqa
from .static import *  # noqa
from .templates import *  # noqa

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
ALLOWED_HOSTS = ['*']
