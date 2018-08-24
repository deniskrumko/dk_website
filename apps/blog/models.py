from django.db import models
from django.utils.translation import ugettext_lazy as _

from adminsortable.models import SortableMixin

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
    wide_image = models.ImageField(
        null=True,
        blank=True,
        upload_to=BaseModel.obfuscated_upload,
        verbose_name=_('Wide image'),
        help_text=_('Image for index page'),
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
    date = models.DateTimeField(
        blank=False,
        verbose_name=_('date'),
    )
    show_gallery = models.BooleanField(
        default=False,
        verbose_name=_('show_gallery'),
    )

    def __str__(self):
        return self.title or '-'

    class Meta:
        verbose_name = _('Blog entry')
        verbose_name_plural = _('Blog entries')
        ordering = ('-date',)


class BlogRelation(SortableMixin, BaseModel):
    blog = models.ForeignKey(
        'blog.BlogEntry',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='relations',
        verbose_name=_('Blog'),
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
        verbose_name=_('Order'),
    )
    related_blog = models.ForeignKey(
        'blog.BlogEntry',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='relations_2',
        verbose_name=_('Related blog'),
    )

    class Meta:
        verbose_name = _('Blog relation')
        verbose_name_plural = _('Blog relations')
        ordering = ('order',)


class BlogImage(SortableMixin, BaseModel):
    """Documentation"""
    blog = models.ForeignKey(
        'blog.BlogEntry',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('blog'),
    )
    image = models.ImageField(
        null=True,
        blank=False,
        upload_to=BaseModel.obfuscated_upload,
        verbose_name=_('image')
    )
    description = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('description'),
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
        verbose_name=_('Order'),
    )

    def __str__(self):
        return str(self.image) or '-'

    class Meta:
        verbose_name = _('BlogImage')
        verbose_name_plural = _('BlogImages')
        ordering = ('order',)
