from django.db import models
from django.utils.translation import ugettext_lazy as _

from adminsortable.models import SortableMixin

from core.models import BaseModel

__all__ = (
    'FileCategory',
    'File'
)


class FileCategory(SortableMixin, BaseModel):
    """Model for file category."""
    name = models.CharField(
        max_length=64,
        null=True,
        blank=False,
        verbose_name=_('Name')
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
        verbose_name=_('Order'),
    )

    def __str__(self):
        return self.name or '-'

    class Meta:
        verbose_name = _('File category')
        verbose_name_plural = _('File categories')
        ordering = ('order',)


class File(BaseModel):
    """Model for storing files in specified categories.

    Attributes:
        name (str): name of file.
        file (File): file itself.
        category (str): category of file.

    """
    name = models.CharField(
        null=True,
        blank=False,
        max_length=255,
        verbose_name=_('Name')
    )
    data = models.FileField(
        null=True,
        blank=False,
        upload_to=BaseModel.default_upload,
        verbose_name=_('Data')
    )
    category = models.ForeignKey(
        FileCategory,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='files',
        verbose_name=_('Category'),
    )

    @property
    def url(self):
        """Shortcut to get file URL."""
        return self.data.url if self.data else None

    def __str__(self):
        return self.name or '-'

    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Files')


class VideoFile(BaseModel):
    VIDEO_FILE = 'file'
    VIDEO_YOUTUBE = 'youtube'

    VIDEO_SOURCES = (
        (VIDEO_FILE, _('File')),
        (VIDEO_YOUTUBE, _('Youtube')),
    )

    name = models.CharField(
        null=True,
        blank=False,
        max_length=255,
        verbose_name=_('Name')
    )
    data_1080 = models.FileField(
        null=True,
        blank=True,
        upload_to=BaseModel.default_upload,
        verbose_name=_('File (1080p)')
    )
    data_720 = models.FileField(
        null=True,
        blank=True,
        upload_to=BaseModel.default_upload,
        verbose_name=_('File (720p)')
    )
    youtube_link = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Youtube code')
    )
    source = models.CharField(
        max_length=64,
        choices=VIDEO_SOURCES,
        default=VIDEO_FILE,
        null=True,
        blank=False,
        verbose_name=_('Source'),
    )
    poster = models.ImageField(
        null=True,
        blank=True,
        upload_to=BaseModel.obfuscated_upload,
        verbose_name=_('Poster image')
    )

    def __str__(self):
        return f'{self.name} ({self.source})'

    class Meta:
        verbose_name = _('Video file')
        verbose_name_plural = _('Video files')
