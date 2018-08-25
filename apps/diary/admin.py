from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import DiaryEntry
from .import_export.resources import DiaryEntryResource


@admin.register(DiaryEntry)
class DiaryEntryAdmin(ImportExportMixin, admin.ModelAdmin):
    """Admin class for ``DiaryEntry`` model."""
    resource_class = DiaryEntryResource

    fields = (
        'author',
        'date',
        'text',
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
