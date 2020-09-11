import factory

from apps.files.factories import FileFactory

from .models import Album, Track, TrackFile

__all__ = (
    'AlbumFactory',
    'TrackFactory',
    'TrackFileFactory',
)


class AlbumFactory(factory.django.DjangoModelFactory):
    """Factory for ``Album`` model."""

    name = factory.sequence(lambda x: f'Album {x}')
    image = factory.django.ImageField(color='#777')
    order = factory.sequence(lambda x: x)
    year = 2019

    class Meta:
        model = Album


class TrackFactory(factory.django.DjangoModelFactory):
    """Factory for ``Track`` model."""

    album = factory.SubFactory(AlbumFactory)
    name = factory.Faker('name')
    file = factory.SubFactory(FileFactory)
    image = factory.django.ImageField(color='#777')
    year = 2019

    class Meta:
        model = Track


class TrackFileFactory(factory.django.DjangoModelFactory):
    """Factory for ``TrackFile`` model."""

    file = factory.SubFactory(FileFactory)
    track = factory.SubFactory(TrackFactory)
    order = factory.sequence(lambda x: x)

    class Meta:
        model = TrackFile
