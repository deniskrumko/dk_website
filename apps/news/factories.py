from django.utils import timezone

import factory

from . import models


class NewsFactory(factory.DjangoModelFactory):
    """Factory for ``News`` model."""

    title = factory.sequence(lambda x: f'News title {x}')
    tab_title = factory.sequence(lambda x: f'Tab title is small {x}')
    image = factory.django.ImageField(color='#777')
    text = factory.Faker('text')
    preview = factory.Faker('text')
    date = timezone.now()

    class Meta:
        model = models.News
