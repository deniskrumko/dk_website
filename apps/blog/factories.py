from django.utils import timezone

import factory

from .models import BlogEntry


class BlogEntryFactory(factory.DjangoModelFactory):
    """Factory for ``BlogEntry`` model."""
    title = factory.sequence(lambda x: f'Title {x}')
    subtitle = factory.sequence(lambda x: f'Subtitle {x}')
    wide_image = factory.django.ImageField(color='black')
    date = timezone.now()

    class Meta:
        model = BlogEntry
