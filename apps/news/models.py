from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel, LikedModel
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


class News(LikedModel, BaseModel):
    image = ProcessedImageField(
        null=True,
        blank=True,
        processors=[ResizeToFit(960, 540)],
        format='JPEG',
        options={'quality': 80},
        upload_to=BaseModel.obfuscated_upload,
        verbose_name=_('Image'),
    )
    title = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('title'),
    )
    tab_title = models.CharField(
        max_length=48,
        null=True,
        blank=False,
        verbose_name=_('tab title'),
        help_text=_('Tab title is displayed on index page')
    )
    preview = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('preview'),
        help_text=_('Preview is displayed on index page')
    )
    text = models.TextField(
        null=True,
        blank=False,
        verbose_name=_('text'),
    )
    date = models.DateTimeField(
        blank=False,
        verbose_name=_('date'),
    )
    link = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('link'),
    )
    tags = models.ManyToManyField(
        'main.Tag',
        blank=True,
        related_name='news',
        verbose_name=_('tags'),
    )

    def __str__(self):
        return self.title or '-'

    class Meta:
        verbose_name = _('News item')
        verbose_name_plural = _('News items')
        ordering = ('-date',)
