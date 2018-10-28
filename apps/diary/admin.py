from django.contrib import admin

from import_export.admin import ImportExportMixin
from .import_export.resources import DiaryEntryResource
from .models import DiaryEntry
from core.admin import BaseModelAdmin


@admin.register(DiaryEntry)
class DiaryEntryAdmin(ImportExportMixin, BaseModelAdmin):
    """Admin class for ``DiaryEntry`` model."""
    # change_list_template = 'admin/import_export/change_list_import_export.html'
    # change_list_template = 'django_object_actions/change_list.html'
    change_list_template = 'admin/import_export_and_actions.html'
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
