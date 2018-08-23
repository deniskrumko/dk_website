from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from django_object_actions import (
    DjangoObjectActions,
    takes_instance_or_queryset,
)

from .models import BlogEntry, BlogImage


class BlogImageInline(admin.StackedInline):
    """Inline class for ``BlogImage`` model."""
    fields = ('image', 'description', 'order')
    readonly_fields = ('order',)
    model = BlogImage
    extra = 0


@admin.register(BlogEntry)
class BlogEntryAdmin(DjangoObjectActions, admin.ModelAdmin):
    """Admin class for ``BlogEntry`` model."""
    fieldsets = (
        (_('Main'), {
            'fields': (
                'title',
                'subtitle',
                'slug',
                'description',
                'wide_image',
                'video',
                'text',
                'date',
                'show_gallery',
            )
        }),
        (_('Created/Modified'), {
            'fields': (
                'created',
                'modified',
            )
        }),
    )
    list_display = (
        'title',
        'slug',
        'created',
        'modified',
    )
    list_filter = (
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
    )
    inlines = (
        BlogImageInline,
    )

    @takes_instance_or_queryset
    def reset_slug(self, request, qs):
        """Action to reset `slug` field for ``Track`` objects."""
        for obj in qs:
            obj.slug = None
            obj.save()

    reset_slug.label = _('Reset slug')
