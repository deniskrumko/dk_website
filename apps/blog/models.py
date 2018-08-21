from django.db import models
from django.utils.translation import ugettext_lazy as _
from libs.autoslug import AutoSlugField

from core.models import BaseModel


class BlogEntry(BaseModel):
    """Documentation"""
    title = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('Title'),
    )
    subtitle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Subtitle'),
    )
    slug = AutoSlugField(
        populate_from='title',
        unique_with=('title',),
        verbose_name=_('Slug'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=_('Short description of blog entry'),
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=BaseModel.obfuscated_upload,
        verbose_name=_('Image')
    )
    video = models.ForeignKey(
        'files.VideoFile',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='blog_enties',
        verbose_name=_('Video'),
    )
    text = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Text'),
        help_text=_('Main blog text')
    )

    def __str__(self):
        return self.title or '-'

    class Meta:
        verbose_name = _('Blog entry')
        verbose_name_plural = _('Blog entries')
        ordering = ('created',)
