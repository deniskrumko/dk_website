from django.contrib import admin
from django.http.response import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from adminsortable.admin import SortableAdmin, SortableTabularInline

from core.admin import BaseModelAdmin, image_preview

from .models import Artist, Track, TrackFile


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """Admin class for ``Artist`` model."""

    list_display = (
        'name',
    )


class TrackFileInline(SortableTabularInline):
    """Inline class for ``TrackFile`` model."""

    model = TrackFile
    fields = (
        'file',
    )
    autocomplete_fields = (
        'file',
    )
    readonly_fields = (
        'order',
    )
    extra = 0


@admin.register(Track)
class TrackAdmin(BaseModelAdmin, SortableAdmin):
    """Admin class for ``Track`` model."""

    url_index = 'music:index'
    url_detail = 'music:detail'

    sortable_change_list_with_sort_link_template = (
        'django_object_actions/change_list.html'
    )
    fieldsets = (
        (_('Main'), {
            'fields': (
                'is_active',
                'artist',
                'name',
                'slug',
                'year',
                'file',
            )
        }),
        (_('Description'), {
            'fields': (
                'short_description',
                'lead',
                'full_description',
            )
        }),
        (_('Image'), {
            'fields': (
                'image',
                '_large_preview',
                'color',
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
        'name',
        'artist',
        'year',
        '_small_preview',
        'slug',
        'order',
    )
    readonly_fields = (
        'slug',
        'created',
        'modified',
        '_small_preview',
        '_large_preview',
    )
    autocomplete_fields = (
        'file',
    )
    search_fields = (
        'artist__name',
        'name',
    )
    inlines = (TrackFileInline,)
    change_actions = (
        'reset_slug',
        'on_site',
    )
    changelist_actions = (
        'reset_slug',
        'on_site',
        'sort_objects',
    )
    ordering = (
        'artist',
        '-order',
    )

    def sort_objects(self, request, queryset):
        """Redirect to sorting page.

        This fix is needed to make ``DjangoObjectActions`` and
        ``SortableAdmin`` classes to work together with template from first
        class.

        """
        return HttpResponseRedirect('/admin/music/track/sort/')

    sort_objects.label = _('Sort objects')

    def _small_preview(self, obj):
        """Get small image preview."""
        return image_preview(obj, size='small', field='image_thumbnail')

    _small_preview.short_description = _('Image preview')

    def _large_preview(self, obj):
        """Get large image preview."""
        return image_preview(obj, size='large', field='image_thumbnail')

    _large_preview.short_description = _('Image preview')
