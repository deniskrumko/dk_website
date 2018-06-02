from django.contrib import admin

from .models import DiaryEntry


@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    """Admin class for ``DiaryEntry`` model."""
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
