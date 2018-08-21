from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import BlogEntry
from django_object_actions import (
    DjangoObjectActions,
    takes_instance_or_queryset,
)


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
                'image',
                'video',
                'text',
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

    @takes_instance_or_queryset
    def reset_slug(self, request, qs):
        """Action to reset `slug` field for ``Track`` objects."""
        for obj in qs:
            obj.slug = None
            obj.save()

    reset_slug.label = _('Reset slug')
