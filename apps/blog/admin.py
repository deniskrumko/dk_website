from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from adminsortable.admin import SortableAdmin, SortableTabularInline

from core.admin import BaseModelAdmin

from . import models


class BlogImageInline(admin.TabularInline):
    """Inline class for ``BlogImage`` model."""

    fields = (
        'image',
        'description',
        'order'
    )
    readonly_fields = (
        'order',
    )
    model = models.BlogImage
    extra = 0


@admin.register(models.BlogEntry)
class BlogEntryAdmin(BaseModelAdmin):
    """Admin class for ``BlogEntry`` model."""

    url_index = 'blog:index'
    url_detail = 'blog:detail'

    fieldsets = (
        (_('Main'), {
            'fields': (
                'is_active',
                'title',
                'subtitle',
                'date',
                'slug',
            )
        }),
        (_('Images'), {
            'fields': (
                'image',
            )
        }),
        (_('Details'), {
            'fields': (
                'video',
                'text',
                'show_gallery',
            )
        }),
        (_('SEO'), {
            'fields': (
                'description',
            )
        }),
        (_('Created/Modified'), {
            'fields': (
                'created',
                'modified',
            )
        }),
    )
    autocomplete_fields = (
        'video',
    )
    list_display = (
        'title',
        'slug',
        'video',
        'date',
        'is_active',
    )
    list_editable = (
        'is_active',
    )
    search_fields = (
        'title',
        'description',
    )
    readonly_fields = (
        'created',
        'modified',
        'slug',
    )
    changelist_actions = (
        'reset_slug',
        'on_site',
    )
    change_actions = (
        'reset_slug',
        'on_site',
    )
    inlines = (
        BlogImageInline,
    )


class BlogSeriesItemInline(SortableTabularInline):
    """Inline class for ``BlogSeriesItem`` model."""

    model = models.BlogSeriesItem
    extra = 0
    fields = (
        'entry',
        'title',
        'order',
    )
    readonly_fields = (
        'order',
    )
    autocomplete_fields = (
        'entry',
    )


@admin.register(models.BlogSeries)
class BlogSeriesAdmin(SortableAdmin):
    """Admin class for ``BlogSeries`` model."""

    fieldsets = (
        (_('Main'), {
            'fields': (
                'name',
            )
        }),
    )
    list_display = (
        'name',
    )
    inlines = (
        BlogSeriesItemInline,
    )
