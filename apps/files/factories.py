import factory

from .models import File, FileCategory

__all__ = (
    'FileFactory',
    'FileCategoryFactory'
)


class FileCategoryFactory(factory.DjangoModelFactory):
    """Factory for ``FileCategory`` model."""
    name = factory.sequence(lambda x: f'Category {x}')
    order = factory.sequence(lambda x: x)

    class Meta:
        model = FileCategory


class FileFactory(factory.DjangoModelFactory):
    """Factory for ``File`` model."""
    name = factory.sequence(lambda x: f'Name {x}')
    category = factory.SubFactory(FileCategoryFactory)
    data = factory.django.FileField()

    class Meta:
        model = File
