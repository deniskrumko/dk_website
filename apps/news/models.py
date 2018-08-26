from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel, LikedModel, register_liked_model


@register_liked_model(name='news')
class News(LikedModel, BaseModel):
    title = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('title'),
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

    def __str__(self):
        return self.title or '-'

    class Meta:
        verbose_name = _('News item')
        verbose_name_plural = _('News items')
        ordering = ('-date',)
