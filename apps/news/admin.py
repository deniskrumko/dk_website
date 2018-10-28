from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from core.admin import BaseModelAdmin

from .models import News


@admin.register(News)
class NewsAdmin(BaseModelAdmin):
    """Admin class for ``News`` model."""

    url_index = 'news:index'
    url_detail = 'news:detail'

    fieldsets = (
        (_('Main'), {
            'fields': (
                'image',
                'title',
                'slug',
                'text',
                'date',
            )
        }),
        (_('Index page'), {
            'fields': (
                'tab_title',
                'preview',
            )
        }),
        (_('Optional'), {
            'fields': (
                'link',
            )
        }),
        (_('Tags'), {
            'fields': (
                'tags',
            )
        }),
    )
    list_display = (
        'title',
        'slug',
        'tab_title',
        'date',
    )
    filter_horizontal = (
        'tags',
    )
    readonly_fields = (
        'slug',
    )
    change_actions = (
        'reset_slug',
        'on_site',
    )
    changelist_actions = (
        'reset_slug',
        'on_site',
    )
