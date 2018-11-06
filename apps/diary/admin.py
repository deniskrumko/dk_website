from django.contrib import admin

from import_export.admin import ImportExportMixin

from core.admin import BaseModelAdmin

from .import_export.resources import DiaryEntryResource
from .models import DiaryEntry, DiaryTag, DiaryTagValue


class DiaryTagValueInline(admin.TabularInline):
    """Inline class for ``DiaryTagValue`` model."""

    model = DiaryTagValue
    extra = 0


@admin.register(DiaryEntry)
class DiaryEntryAdmin(ImportExportMixin, BaseModelAdmin):
    """Admin class for ``DiaryEntry`` model."""

    change_list_template = 'admin/import_export_and_actions.html'
    resource_class = DiaryEntryResource
    sortable_by = 'date'
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
    inlines = (
        DiaryTagValueInline,
    )


@admin.register(DiaryTag)
class DiaryTagAdmin(admin.ModelAdmin):
    """Admin class for ``DiaryTag`` model."""

    pass


@admin.register(DiaryTagValue)
class DiaryTagValueAdmin(admin.ModelAdmin):
    """Admin class for ``DiaryTagValue`` model."""

    pass
