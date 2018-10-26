import factory

from . import models

__all__ = (
    'FileFactory',
    'FileCategoryFactory',
    'VideoFileFactory',
)


class FileCategoryFactory(factory.DjangoModelFactory):
    """Factory for ``FileCategory`` model."""

    name = factory.sequence(lambda x: f'Category {x}')
    order = factory.sequence(lambda x: x)

    class Meta:
        model = models.FileCategory


class FileFactory(factory.DjangoModelFactory):
    """Factory for ``File`` model."""

    name = factory.sequence(lambda x: f'Name {x}')
    category = factory.SubFactory(FileCategoryFactory)
    data = factory.django.FileField()

    class Meta:
        model = models.File


class VideoFileFactory(factory.DjangoModelFactory):
    """Factory for ``VideoFile`` model."""

    name = factory.sequence(lambda x: f'Video {x}')
    source_original = 'http://techslides.com/demos/sample-videos/small.mp4'
    source_1080 = 'http://techslides.com/demos/sample-videos/small.mp4'
    source_720 = 'http://techslides.com/demos/sample-videos/small.mp4'
    source_480 = 'http://techslides.com/demos/sample-videos/small.mp4'
    source_360 = 'http://techslides.com/demos/sample-videos/small.mp4'
    poster = factory.django.ImageField(color='#1D252C')

    class Meta:
        model = models.VideoFile
