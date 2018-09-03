from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from core.admin import BaseModelAdmin

from .models import BlogEntry, BlogImage, BlogRelation


class BlogImageInline(admin.StackedInline):
    """Inline class for ``BlogImage`` model."""
    fields = ('image', 'description', 'order')
    readonly_fields = ('order',)
    model = BlogImage
    extra = 0


class BlogRelationInline(admin.TabularInline):
    """Inline class for ``BlogRelation`` model."""
    model = BlogRelation
    fields = ('related_blog', 'order')
    autocomplete_fields = (
        'related_blog',
    )
    fk_name = 'blog'
    readonly_fields = ('order',)
    extra = 0


@admin.register(BlogEntry)
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
        (_('On list page'), {
            'fields': (
                'wide_image',
            )
        }),
        (_('On details page'), {
            'fields': (
                'video',
                'text',
                'show_gallery',
            )
        }),
        (_('Next/previous'), {
            'fields': (
                'next_part',
                'prev_part',
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
        'next_part',
        'prev_part',
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
        BlogRelationInline,
    )
