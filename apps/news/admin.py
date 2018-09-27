from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Admin class for ``News`` model."""
    fieldsets = (
        (_('Main'), {
            'fields': (
                'title',
                'text',
                'date',
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
    )
    filter_horizontal = (
        'tags',
    )
