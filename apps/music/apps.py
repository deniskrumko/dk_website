from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MusicConfig(AppConfig):
    """Configuration for ``Music`` app."""
    name = 'apps.music'
    verbose_name = _('Music')
