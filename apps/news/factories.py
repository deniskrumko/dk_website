from django.utils import timezone

import factory

from . import models


class NewsFactory(factory.DjangoModelFactory):
    """Factory for ``News`` model."""
    title = factory.sequence(lambda x: f'Title {x}')
    text = factory.Faker('text')
    date = timezone.now()

    class Meta:
        model = models.News
