from typing import Any

from django.contrib import admin
from django.shortcuts import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from core.admin import BaseModelAdmin

from .models import DiaryEntry, DiaryTag, DiaryTagGroup, DiaryTagValue


class PrivateQuerySetMixin:
    """Allow to view only own diary entries."""

    private_queryset_field = 'author'

    def get_queryset(self, request):
        qs = super().get_queryset(request)  # type: ignore
        params = {self.private_queryset_field: request.user}
        return qs.filter(**params)


class DiaryTagValueInline(admin.TabularInline):
    """Inline class for ``DiaryTagValue`` model."""

    model = DiaryTagValue
    extra = 0
    readonly_fields = (
        'author',
        'tag',
        'value',
    )

    def has_delete_permission(self, *args: Any, **kwargs: Any) -> bool:
        """Forbid to delete objects."""
        return False

    def has_add_permission(self, *args: Any, **kwargs: Any) -> bool:
        """Forbid to add objects."""
        return False


@admin.register(DiaryEntry)
class DiaryEntryAdmin(PrivateQuerySetMixin, BaseModelAdmin):
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

    def reverse_url_detail_args(self, obj: DiaryEntry) -> tuple:
        return (obj.date,)

    def _preview(self, obj: DiaryEntry) -> str:
        return str(obj.text[:50] + '...') if obj.text else '-'

    _preview.short_description = _('Preview')


@admin.register(DiaryTag)
class DiaryTagAdmin(PrivateQuerySetMixin, admin.ModelAdmin):
    """Admin class for ``DiaryTag`` model."""

    list_display = (
        'name',
        'group',
        'values_count',
    )
    list_filter = (
        'group',
    )
    search_fields = (
        'name',
    )
    readonly_fields = (
        'group',
        'values_count',
    )

    def get_actions(self, *args: Any, **kwargs: Any) -> list:
        """Forbid any actions."""
        return []

    def values_count(self, obj: DiaryTag) -> Any:
        """Get number of diary tag values."""
        count = obj.values.count()
        url = reverse('diary:tag', args=(obj.name,))
        return mark_safe(f'<a href="{url}" target="_blank">{count}</a>')

    values_count.short_description = _('Количество записей')


@admin.register(DiaryTagValue)
class DiaryTagValueAdmin(PrivateQuerySetMixin, BaseModelAdmin):
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

    def has_delete_permission(self, *args: Any, **kwargs: Any) -> bool:
        """Forbid to delete objects."""
        return False

    def has_add_permission(self, *args: Any, **kwargs: Any) -> bool:
        """Forbid to add objects."""
        return False

    def has_change_permission(self, *args: Any, **kwargs: Any) -> bool:
        """Forbid to change objects."""
        return False

    def redirect_to_entry(self, request, obj):
        return self.redirect(obj.entry.admin_changelink)

    redirect_to_entry.label = _('Go to entry')
    redirect_to_entry.short_description = _('Go to entry')


class DiaryTagInline(admin.TabularInline):
    """Inline class for ``DiaryTag`` model."""

    model = DiaryTag
    extra = 0

    def has_add_permission(self, *args: Any, **kwargs: Any) -> bool:
        """Forbid to add objects."""
        return False

    def has_change_permission(self, *args: Any, **kwargs: Any) -> bool:
        """Forbid to change objects."""
        return False


@admin.register(DiaryTagGroup)
class DiaryTagGroupAdmin(PrivateQuerySetMixin, BaseModelAdmin):
    """Admin class for ``DiaryTagGroup`` model."""

    list_display = (
        'name',
        'color',
        'order',
    )
    search_fields = (
        'name',
    )
    readonly_fields = (
        'author',
    )
    inlines = (
        DiaryTagInline,
    )

    def save_model(self, request, obj, form, change):
        """Save model and set author."""
        if not obj.author:
            obj.author = request.user

        return super().save_model(request, obj, form, change)
