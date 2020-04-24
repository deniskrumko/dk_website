import factory

from . import models


class DiaryEntryFactory(factory.DjangoModelFactory):
    """Factory for ``DiaryEntry`` model."""

    text = factory.Faker('text', max_nb_chars=1000, locale='ru_RU')
    done = factory.sequence(lambda x: bool(x % 5))

    class Meta:
        model = models.DiaryEntry


class DiaryTagFactory(factory.DjangoModelFactory):
    """Factory for ``DiaryTag`` model."""

    name = factory.Faker('word', locale='ru_RU')

    class Meta:
        model = models.DiaryTag
        django_get_or_create = ('name',)
