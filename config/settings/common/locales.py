import os

from django.utils.translation import ugettext_lazy as _

from .paths import BASE_DIR

LANGUAGE_CODE = 'ru-RU'
LANGUAGES = [('ru', _('Russian'))]

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locales')
]
