from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MainConfig(AppConfig):
    """Configuration for ``Main`` app."""

    name = 'apps.main'
    verbose_name = _('Main')
