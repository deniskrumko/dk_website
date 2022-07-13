from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import DiaryEntry, DiaryTag


@receiver(post_save, sender=DiaryEntry)
def populate_tags_signal(instance, created, *args, **kwargs):
    """Create tags on diary entry save."""
    instance.populate_tags()


@receiver(pre_delete, sender=DiaryTag)
def remove_diary_tag(instance, *args, **kwargs):
    """Remove diary tag with all values."""
    # Clean each entry from this tag
    for entry in instance.entries.all():
        result_text = []
        for line in entry.text.split('\r\n'):
            if not line.startswith(f'#{instance.name}'):
                result_text.append(line)

        entry.text = '\r\n'.join(result_text)
        entry.save()

    # Delete values manually
    instance.values.all().delete()
