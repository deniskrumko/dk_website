from uuid import uuid4

from django.shortcuts import reverse

from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    """Base class for models."""

    class Meta:
        abstract = True

    @classmethod
    def default_upload(cls, instance, filename):
        """Get default file upload handler.

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

    @property
    def admin_changelink(self):
        """Shortcut to get link for change object page in Django Admin.

        Example:
            # file_instance.id = 1
            self.get_change_link(model_class=File, obj=file_instance)

        Returns:
            '/admin/file_storage/file/1/'

        """
        return reverse(
            'admin:{meta.app_label}_{meta.model_name}_change'
            .format(meta=self.__class__._meta), args=(self.id,)
        )
