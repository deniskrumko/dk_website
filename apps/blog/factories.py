from datetime import timedelta

from django.utils import timezone

import factory

from apps.files.factories import VideoFileFactory

from . import models


class BlogImageFactory(factory.DjangoModelFactory):
    """Factory for ``BlogImage`` model."""

    description = factory.sequence(lambda x: f'Title {x}')
    image = factory.django.ImageField(color='#333')
    order = factory.sequence(lambda x: x)

    class Meta:
        model = models.BlogImage


class BlogEntryFactory(factory.DjangoModelFactory):
    """Factory for ``BlogEntry`` model."""

    date = factory.sequence(lambda x: timezone.now() + timedelta(days=x))
    description = factory.sequence(lambda x: f'SEO description {x}')
    show_gallery = True
    subtitle = factory.Faker('sentence')
    text = factory.Faker('text')
    title = factory.sequence(lambda x: f'Фильм {x}. Часть 2')
    video = factory.SubFactory(VideoFileFactory)

    @factory.post_generation
    def create_images(self, create, extracted, **kwargs):
        """Create images for blog."""
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # Create 6 images
            BlogImageFactory.create_batch(2, blog=self)

    class Meta:
        model = models.BlogEntry
