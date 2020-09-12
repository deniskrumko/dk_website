from django.db import models
from django.utils.translation import ugettext_lazy as _

from adminsortable.models import SortableMixin
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFit

from core.models import BaseModel, LikedModel


class BlogEntry(LikedModel, BaseModel):
    """Model to store one blog entry."""

    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Is active'),
    )
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
    slug = models.CharField(
        blank=False,
        db_index=True,
        max_length=64,
        null=True,
        unique=True,
        verbose_name=_('Slug'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=_('Short description of blog entry'),
    )
    image = ProcessedImageField(
        null=True,
        blank=True,
        processors=[ResizeToFit(960, 540)],
        format='JPEG',
        options={'quality': 100},
        upload_to=BaseModel.obfuscated_upload,
        verbose_name=_('Image'),
    )
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(400, 400)],
        format='JPEG',
        options={'quality': 100},
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
        help_text=_('Main blog text'),
    )
    date = models.DateTimeField(
        blank=False,
        verbose_name=_('Date'),
    )
    show_gallery = models.BooleanField(
        default=False,
        verbose_name=_('Show gallery'),
    )

    def __str__(self):
        return self.title or '-'

    class Meta:
        verbose_name = _('Blog entry')
        verbose_name_plural = _('Blog entries')
        ordering = ('-date',)

    def get_absolute_url(self):
        """Get absolute URL for sitemap."""
        return f'/blog/{self.slug}'

    # Blog series navigation
    # ========================================================================

    @property
    def is_series(self):
        return self.series_item.exists()

    @property
    def series(self):
        return self.series_item.first().series

    @property
    def next(self):
        return self._get_part(index=1)

    @property
    def prev(self):
        return self._get_part(index=-1)

    @property
    def duration(self):
        """Get video duration if it exists."""
        return self.video.duration if self.video else None

    def _get_part(self, index):
        order = self.series_item.first().order + index
        return self.series.items.filter(order=order).first()


class BlogSeries(BaseModel):
    """Model for blog series."""

    name = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('Name'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Blog series')
        verbose_name_plural = _('Blog series')


class BlogSeriesItem(SortableMixin, BaseModel):
    """Model for item in blog series."""

    series = models.ForeignKey(
        BlogSeries,
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name=_('Series'),
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
        verbose_name=_('Order'),
    )
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Custom title'),
    )
    entry = models.ForeignKey(
        BlogEntry,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='series_item',
        verbose_name=_('Blog'),
    )

    def __str__(self):
        return self.title or self.entry.title

    class Meta:
        verbose_name = _('Blog entry')
        verbose_name_plural = _('Blog entries')
        ordering = ('order',)


class BlogImage(SortableMixin, BaseModel):
    """Model to store one image for blog.

    Each blog can have related imaged (more often - trip photos).

    """

    blog = models.ForeignKey(
        'blog.BlogEntry',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('Blog'),
    )
    image = ProcessedImageField(
        null=True,
        blank=False,
        processors=[ResizeToFit(1500, 1500)],
        format='JPEG',
        options={'quality': 80},
        upload_to=BaseModel.obfuscated_upload,
        verbose_name=_('Image'),
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(150, 150)],
        format='JPEG',
        options={'quality': 80},
    )
    description = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Description'),
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
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        ordering = ('order',)
