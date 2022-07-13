from datetime import timedelta
from typing import Any

from django.utils import timezone

import factory

from apps.files.factories import VideoFileFactory

from . import models


class BlogImageFactory(factory.django.DjangoModelFactory):
    """Factory for ``BlogImage`` model."""

    description = factory.sequence(lambda x: f'Title {x}')
    image = factory.django.ImageField(color='#333')
    order = factory.sequence(lambda x: x)

    class Meta:
        model = models.BlogImage


class BlogEntryFactory(factory.django.DjangoModelFactory):
    """Factory for ``BlogEntry`` model."""

    date = factory.sequence(lambda x: timezone.now() + timedelta(days=x))
    description = factory.sequence(lambda x: f'SEO description {x}')
    show_gallery = True
    subtitle = factory.Faker('sentence')
    text = factory.Faker('text')
    title = factory.sequence(lambda x: f'Блог {x}')
    video = factory.SubFactory(VideoFileFactory)
    slug = factory.sequence(lambda x: f'blog-{x}')

    @factory.post_generation  # type: ignore
    def create_images(self, create: bool, extracted: bool, **kwargs: Any) -> None:
        """Create images for blog."""
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # Create 6 images
            BlogImageFactory.create_batch(2, blog=self)

    class Meta:
        model = models.BlogEntry


class BlogSeriesFactory(factory.django.DjangoModelFactory):
    """Factory for ``BlogSeries`` model."""

    name = factory.sequence(lambda x: f'Series {x}')

    class Meta:
        model = models.BlogSeries


class BlogSeriesItemFactory(factory.django.DjangoModelFactory):
    """Factory for ``BlogSeriesItem`` model."""

    title = factory.sequence(lambda x: f'Title {x}')

    class Meta:
        model = models.BlogSeriesItem
