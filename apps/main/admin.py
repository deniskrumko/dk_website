from django.contrib import admin
from .models import RedirectPage
from django.utils.translation import ugettext_lazy as _


@admin.register(RedirectPage)
class RedirectPageAdmin(admin.ModelAdmin):
    """Admin class for ``RedirectPage`` model."""
    list_display = (
        'source',
        'destination',
        '_result',
    )
    readonly_fields = (
        '_result',
    )

    def _result(self, obj):
        return f'http://deniskrumko.ru/go/{obj.source}'

    _result.short_description = _('Result')
