import factory

from . import models

__all__ = (
    'FileFactory',
    'FileCategoryFactory',
    'VideoFileFactory',
)


class FileCategoryFactory(factory.django.DjangoModelFactory):
    """Factory for ``FileCategory`` model."""

    name = factory.sequence(lambda x: f'Category {x}')
    order = factory.sequence(lambda x: x)

    class Meta:
        model = models.FileCategory


class FileFactory(factory.django.DjangoModelFactory):
    """Factory for ``File`` model."""

    name = factory.sequence(lambda x: f'Name {x}')
    category = factory.SubFactory(FileCategoryFactory)
    data = factory.django.FileField()

    class Meta:
        model = models.File


class VideoFileFactory(factory.django.DjangoModelFactory):
    """Factory for ``VideoFile`` model."""

    name = factory.sequence(lambda x: f'Video {x}')
    source_original = 'http://techslides.com/demos/sample-videos/small.mp4'
    source_1080 = 'http://techslides.com/demos/sample-videos/small.mp4'
    source_720 = 'http://techslides.com/demos/sample-videos/small.mp4'
    source_480 = 'http://techslides.com/demos/sample-videos/small.mp4'
    source_360 = 'http://techslides.com/demos/sample-videos/small.mp4'
    youtube_link = 'https://www.youtube.com/watch?v=yoyrUrTN7Xw'
    poster = factory.django.ImageField(color='#E06C75', width=1280, height=720)
    duration = '12:34'

    class Meta:
        model = models.VideoFile
