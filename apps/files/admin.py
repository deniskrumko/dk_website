from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from . import forms, models


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    """Admin class for ``File`` model."""

    list_display = (
        'name',
        'data',
        'category',
        'created',
    )
    autocomplete_fields = (
        'category',
    )
    search_fields = (
        'name',
    )


@admin.register(models.FileCategory)
class FileCategoryAdmin(admin.ModelAdmin):
    """Admin class for ``FileCategory`` model."""

    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )


@admin.register(models.VideoFile)
class VideoFileAdmin(admin.ModelAdmin):
    """Admin class for ``VideoFile`` model."""

    form = forms.VideoFileForm
    fieldsets = (
        (_('Main'), {
            'fields': (
                'name',
                'source',
                'poster',
            )
        }),
        (_('Sources'), {
            'fields': (
                'source_original',
                'source_1080',
                'source_720',
                'source_480',
                'source_360',
            )
        }),
        (_('YouTube'), {
            'fields': (
                'youtube_link',
            )
        }),
    )
    list_display = (
        'name',
        'source',
        '_original',
        '_1080',
        '_720',
        '_480',
        '_360',
    )
    search_fields = (
        'name',
    )

    def _original(self, obj):
        return bool(obj.source_original)

    _original.short_description = _('Original')
    _original.boolean = True

    def _1080(self, obj):
        return bool(obj.source_1080)

    _1080.short_description = _('1080p')
    _1080.boolean = True

    def _720(self, obj):
        return bool(obj.source_720)

    _720.short_description = _('720p')
    _720.boolean = True

    def _480(self, obj):
        return bool(obj.source_480)

    _480.short_description = _('480p')
    _480.boolean = True

    def _360(self, obj):
        return bool(obj.source_360)

    _360.short_description = _('360p')
    _360.boolean = True
