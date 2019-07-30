from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFit

from core.models import BaseModel


class User(AbstractUser):
    """Model for app user."""

    email = models.EmailField(
        _('email address'),
        blank=False,
        unique=True
    )
    image = ProcessedImageField(
        null=True,
        blank=True,
        processors=[ResizeToFit(800, 800)],
        format='JPEG',
        options={'quality': 100},
        upload_to=BaseModel.obfuscated_upload,
        verbose_name=_('Image'),
    )
    image_small = ImageSpecField(
        source='image',
        processors=[ResizeToFit(100, 100)],
        format='JPEG',
        options={'quality': 80}
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ('email',)

    @property
    def full_name(self):
        """Get full name of user."""
        return f'{self.first_name} {self.last_name}'
