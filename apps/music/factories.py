import factory

from apps.files.factories import FileFactory

from .models import Album, MusicVideo, Track, TrackFile

__all__ = (
    'AlbumFactory',
    'MusicVideoFactory',
    'TrackFactory',
    'TrackFileFactory',
)


class AlbumFactory(factory.django.DjangoModelFactory):
    """Factory for ``Album`` model."""

    name = factory.sequence(lambda x: f'Album {x}')
    slug = factory.sequence(lambda x: f'album-{x}')
    image = factory.django.ImageField(color='#777')
    order = factory.sequence(lambda x: x)
    year = 2019

    class Meta:
        model = Album


class TrackFactory(factory.django.DjangoModelFactory):
    """Factory for ``Track`` model."""

    album = factory.SubFactory(AlbumFactory)
    name = factory.Faker('name')
    slug = factory.sequence(lambda x: f'track-{x}')
    file = factory.SubFactory(FileFactory)
    image = factory.django.ImageField(color='#98C379', width=400, height=400)

    class Meta:
        model = Track


class TrackFileFactory(factory.django.DjangoModelFactory):
    """Factory for ``TrackFile`` model."""

    file = factory.SubFactory(FileFactory)
    track = factory.SubFactory(TrackFactory)
    order = factory.sequence(lambda x: x)

    class Meta:
        model = TrackFile


class MusicVideoFactory(factory.django.DjangoModelFactory):
    """Factory for ``MusicVideo`` model."""

    is_active = True
    name = factory.sequence(lambda x: f'Music Video {x}')
    slug = factory.sequence(lambda x: f'music-video-{x}')

    class Meta:
        model = MusicVideo
