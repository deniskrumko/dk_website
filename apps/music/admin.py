from django.contrib import admin
from django.http.response import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from adminsortable.admin import SortableAdmin, SortableTabularInline

from core.admin import BaseModelAdmin, image_preview

from .forms import TrackForm
from .models import Album, Track, TrackFile


class TrackInline(admin.TabularInline):
    """Inline class for ``Track`` model."""

    model = Track
    form = TrackForm
    fields = (
        'name',
        'year',
        'duration',
        'order',
        'is_active',
    )
    readonly_fields = (
        'order',
    )
    extra = 0


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """Admin class for ``Album`` model."""

    fieldsets = (
        (_('Main'), {
            'fields': (
                'name',
                'slug',
                'year',
                'image',
                '_large_preview',
            )
        }),
        (_('About album'), {
            'fields': (
                'status',
                '_duration',
                '_tracks_count',
                'order',
            )
        }),
    )
    list_display = (
        'name',
        'year',
        '_small_preview',
        '_tracks_count',
        'order',
        '_duration',
        'status',
    )
    readonly_fields = (
        'order',
        'slug',
        '_tracks_count',
        '_duration',
        '_large_preview',
    )
    inlines = (
        TrackInline,
    )
    search_fields = (
        'name',
        'slug',
    )

    def _small_preview(self, obj):
        """Get small image preview."""
        return image_preview(obj, size='small', field='image')

    _small_preview.short_description = _('Image preview')

    def _large_preview(self, obj):
        """Get large image preview."""
        return image_preview(obj, size='large', field='image')

    _large_preview.short_description = _('Image preview')

    def _duration(self, obj):
        """Get duration of all tracks."""
        return obj.displayed_duration

    _duration.short_description = _('Duration')

    def _tracks_count(self, obj):
        """Get count of all tracks."""
        return obj.tracks_count

    _tracks_count.short_description = _('Tracks count')


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

    form = TrackForm
    sortable_change_list_with_sort_link_template = (
        'django_object_actions/change_list.html'
    )
    fieldsets = (
        (_('Main'), {
            'fields': (
                'is_active',
                'album',
                'name',
                'slug',
                'year',
                'duration',
                'file',
            )
        }),
        (_('Image'), {
            'fields': (
                'image',
                '_large_preview',
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
        'album',
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
        'album__name',
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
