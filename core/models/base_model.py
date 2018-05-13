from uuid import uuid4

from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    """Base class for models."""

    class Meta:
        abstract = True

    @classmethod
    def default_upload(cls, instance, filename):
        """Default file upload handler.

        Saves file with original name and extension.

        """
        folder = instance._meta.model_name.replace(' ', '-')
        return f'{folder}/{filename}'

    @classmethod
    def obfuscated_upload(cls, instance, filename):
        """Obfuscated file upload handler.

        Saves file with obfuscated name (UUID) and original extension.

        """
        folder = instance._meta.model_name.replace(' ', '-')
        extension = filename.split('.')[-1]
        return f'{folder}/{uuid4()}.{extension}'
