from django.contrib import admin

from import_export.admin import ImportExportMixin

from core.admin import BaseModelAdmin

from .import_export.resources import DiaryEntryResource
from .models import DiaryEntry, DiaryTag, DiaryTagValue


class PrivateQuerySet(object):
    """Allow to view only own diary entries."""

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(author=request.user)


class DiaryTagValueInline(admin.TabularInline):
    """Inline class for ``DiaryTagValue`` model."""

    model = DiaryTagValue
    extra = 0


@admin.register(DiaryEntry)
class DiaryEntryAdmin(ImportExportMixin, PrivateQuerySet, BaseModelAdmin):
    """Admin class for ``DiaryEntry`` model."""

    change_list_template = 'admin/import_export_and_actions.html'
    resource_class = DiaryEntryResource
    url_index = 'diary:index'
    url_detail = 'diary:detail'
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

    def get_export_queryset(self, request):
        qs = super().get_export_queryset(request)
        return qs.filter(author=request.user)

    def get_urls(self):
        """Prepend `get_urls` with our own patterns."""
        urls1 = super(ImportExportMixin, self).get_urls()
        urls2 = super(BaseModelAdmin, self).get_urls()
        return urls1 + urls2

    def reverse_url_detail_args(self, obj):
        return (obj.date,)


@admin.register(DiaryTag)
class DiaryTagAdmin(PrivateQuerySet, admin.ModelAdmin):
    """Admin class for ``DiaryTag`` model."""

    list_display = (
        'name',
        'author',
    )
    search_fields = (
        'name',
    )


@admin.register(DiaryTagValue)
class DiaryTagValueAdmin(PrivateQuerySet, admin.ModelAdmin):
    """Admin class for ``DiaryTagValue`` model."""

    list_display = (
        'tag',
        'author',
        'entry',
        'value',
    )
    autocomplete_fields = (
        'author',
        'entry',
        'tag',
    )
