from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import RedirectPage, Tag


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


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin class for ``Tag`` model."""
    fieldsets = (
        (_('Main'), {
            'fields': (
                'name',
                'slug',
                'color',
                'background',
            )
        }),
    )
    list_display = (
        'name',
        'slug',
        'color',
        'background',
    )
    search_fields = (
        'name',
    )
    readonly_fields = (
        'slug',
    )
