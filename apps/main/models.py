from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel


class RedirectPage(BaseModel):
    """Documentation"""
    source = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        db_index=True,
        unique=True,
        verbose_name=_('Source'),
    )
    destination = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('Destination'),
    )

    def __str__(self):
        return f'{self.source} - {self.destination}'

    class Meta:
        verbose_name = _('Redirect page')
        verbose_name_plural = _('Redirect pages')
