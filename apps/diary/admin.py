from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from core.admin import BaseModelAdmin

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
    readonly_fields = (
        'author',
        'tag',
        'value',
    )

    def has_delete_permission(self, *args, **kwargs):
        return False

    def has_add_permission(self, *args, **kwargs):
        return False


@admin.register(DiaryEntry)
class DiaryEntryAdmin(PrivateQuerySet, BaseModelAdmin):
    """Admin class for ``DiaryEntry`` model."""

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
        '_preview',
        'done',
    )
    list_filter = (
        'done',
    )
    readonly_fields = (
        'author',
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
        """Get queryset for items exporting."""
        qs = super().get_export_queryset(request)
        return qs.filter(author=request.user)

    def reverse_url_detail_args(self, obj):
        return (obj.date,)

    def _preview(self, obj):
        return (obj.text[:50] + '...') if obj.text else '-'

    _preview.short_description = _('Preview')


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
class DiaryTagValueAdmin(PrivateQuerySet, BaseModelAdmin):
    """Admin class for ``DiaryTagValue`` model."""

    list_display = (
        'tag',
        'value',
        'entry',
    )
    list_filter = (
        'tag',
    )
    readonly_fields = (
        'value',
        'author',
        'entry',
        'tag',
    )
    change_actions = (
        'redirect_to_entry',
    )

    def has_delete_permission(self, *args, **kwargs):
        return False

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_change_permission(self, *args, **kwargs):
        return False

    def redirect_to_entry(self, request, obj):
        return self.redirect(obj.entry.admin_changelink)

    redirect_to_entry.label = _('Go to entry')
    redirect_to_entry.short_description = _('Go to entry')
