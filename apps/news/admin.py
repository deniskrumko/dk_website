from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Admin class for ``News`` model."""
    list_display = (
        'title',
    )
