from django.contrib import admin
from django.http.response import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from django_object_actions import (
    DjangoObjectActions,
    takes_instance_or_queryset,
)
from import_export.admin import ImportExportMixin

from .import_export.resources import DiaryEntryResource
from .models import DiaryEntry


@admin.register(DiaryEntry)
class DiaryEntryAdmin(
    DjangoObjectActions,
    ImportExportMixin,
    admin.ModelAdmin
):
    """Admin class for ``DiaryEntry`` model."""

    resource_class = DiaryEntryResource
    fields = (
        'author',
        'date',
        'text',
        'files',
        'done',
    )
    list_display = (
        'date',
        'author',
        'created',
        'modified',
    )
    search_fields = (
        'text',
    )
    autocomplete_fields = (
        'files',
    )
    change_actions = (
        'on_site',
    )
    changelist_actions = (
        'on_site',
    )

    @takes_instance_or_queryset
    def on_site(self, request, qs=None):
        """View tracks or one track on site."""
        if qs.count() > 1:
            return HttpResponseRedirect('/diary/')

        entry = qs.first()
        return HttpResponseRedirect(f'/diary/{entry.date}/')

    on_site.label = _('View on site')
