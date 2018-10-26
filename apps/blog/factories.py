from datetime import timedelta

from django.utils import timezone

import factory

from apps.files.factories import VideoFileFactory

from . import models


class BlogRelationFactory(factory.DjangoModelFactory):
    """Factory for ``BlogRelation`` model."""

    order = factory.sequence(lambda x: x)

    class Meta:
        model = models.BlogRelation


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
    wide_image = factory.django.ImageField(color='#555')

    @factory.post_generation
    def create_images(self, create, extracted, **kwargs):
        """Create images for blog."""
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # Create 6 images
            BlogImageFactory.create_batch(2, blog=self)

    @factory.post_generation
    def create_items(self, create, extracted, **kwargs):
        """Create extra blogs for blog."""
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # Create next part
            self.next_part = BlogEntryFactory(
                title=self.title[:-1] + '3',
                date=self.date + timedelta(hours=1),
                prev_part=self,
                create_images=True,
            )

            # Create previous part
            self.prev_part = BlogEntryFactory(
                title=self.title[:-1] + '1',
                date=self.date - timedelta(hours=1),
                next_part=self,
                create_images=True
            )

            BlogRelationFactory(
                blog=self,
                related_blog=self.next_part
            )
            BlogRelationFactory(
                blog=self,
                related_blog=self.prev_part
            )
            BlogRelationFactory(
                blog=self.prev_part,
                related_blog=self
            )
            BlogRelationFactory(
                blog=self.prev_part,
                related_blog=self.next_part
            )
            BlogRelationFactory(
                blog=self.next_part,
                related_blog=self
            )
            BlogRelationFactory(
                blog=self.next_part,
                related_blog=self.prev_part
            )

    class Meta:
        model = models.BlogEntry
