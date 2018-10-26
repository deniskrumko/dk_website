from django.contrib import admin
from django.http.response import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from django_object_actions import (
    DjangoObjectActions,
    takes_instance_or_queryset,
)

from .models import News


@admin.register(News)
class NewsAdmin(DjangoObjectActions, admin.ModelAdmin):
    """Admin class for ``News`` model."""

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

    @takes_instance_or_queryset
    def reset_slug(self, request, qs):
        """Reset `slug` field for ``Track`` objects."""
        for obj in qs:
            obj.slug = None
            obj.save()

    reset_slug.label = _('Reset slug')

    @takes_instance_or_queryset
    def on_site(self, request, qs=None):
        """View tracks or one track on site."""
        if qs.count() > 1:
            return HttpResponseRedirect('/news/')

        item = qs.first()
        return HttpResponseRedirect(f'/news/{item.slug}/')

    on_site.label = _('View on site')
