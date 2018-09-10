import factory

from apps.files.factories import FileFactory

from .models import Artist, Track, TrackFile

__all__ = (
    'ArtistFactory',
    'TrackFactory',
    'TrackFileFactory'
)


class ArtistFactory(factory.DjangoModelFactory):
    """Factory for ``Artist`` model."""
    name = factory.Faker('name')
    order = factory.sequence(lambda x: x)

    class Meta:
        model = Artist


class TrackFactory(factory.DjangoModelFactory):
    """Factory for ``Track`` model."""
    artist = factory.SubFactory(ArtistFactory)
    name = factory.Faker('name')
    short_description = factory.Faker('text')
    full_description = factory.Faker('text')
    file = factory.SubFactory(FileFactory)
    image = factory.django.ImageField(color='#777')
    year = 2018

    class Meta:
        model = Track


class TrackFileFactory(factory.DjangoModelFactory):
    """Factory for ``TrackFile`` model."""
    file = factory.SubFactory(FileFactory)
    track = factory.SubFactory(TrackFactory)
    order = factory.sequence(lambda x: x)

    class Meta:
        model = TrackFile
