from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import DiaryEntry


@receiver(post_save, sender=DiaryEntry)
def populate_tags_signal(instance, created, *args, **kwargs):
    """Create tags on diary entry save."""
    instance.populate_tags()
