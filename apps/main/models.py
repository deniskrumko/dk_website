from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel


class RedirectPage(BaseModel):
    """Model to store redirect pages.

    Redirect pages works as short URLs to site content.

    Example:
        source = "vnc"
        destination = "/blog/17daysinvenice"

    Will redirect from "dk.ru/go/vnc" to "dk.ru/blog/17daysinvenice".

    """

    source = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        db_index=True,
        unique=True,
        verbose_name=_('Short URL'),
    )
    destination = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('Full path'),
    )

    def __str__(self):
        return f'{self.source} - {self.destination}'

    class Meta:
        verbose_name = _('Redirect page')
        verbose_name_plural = _('Redirect pages')


class Tag(BaseModel):
    """Model for tags."""

    name = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        unique=True,
        verbose_name=_('Name')
    )
    slug = models.CharField(
        blank=False,
        db_index=True,
        max_length=64,
        null=True,
        unique=True,
        verbose_name=_('Slug'),
    )
    color = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('color'),
        help_text=_('Text color: #FFF')
    )
    background = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('background'),
        help_text=_('Background color: #FFF')
    )

    def __str__(self):
        return self.name or '-'

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
        ordering = ('name',)
