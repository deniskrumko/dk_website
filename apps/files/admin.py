from django.contrib import admin

from .models import File, FileCategory


@admin.register(File)
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


@admin.register(FileCategory)
class FileCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )
