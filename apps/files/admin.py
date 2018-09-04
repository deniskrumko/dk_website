from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from . import forms, models


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
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
        'source_1080',
    )
    search_fields = (
        'name',
    )
