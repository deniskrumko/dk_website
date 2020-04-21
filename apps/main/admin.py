from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from .models import RedirectPage, Tag


@admin.register(RedirectPage)
class RedirectPageAdmin(admin.ModelAdmin):
    """Admin class for ``RedirectPage`` model."""

    list_display = (
        'source',
        'destination',
        'link_preview',
    )
    readonly_fields = (
        'link_preview',
    )

    def link_preview(self, obj: RedirectPage) -> str:
        """Clickable link preview."""
        if not obj.source:
            return '-'

        link = settings.WEBSITE_URL + '/go/' + obj.source
        return mark_safe(f'<a href="{link}">{link}</a>')

    link_preview.short_description = _('Link preview')


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
