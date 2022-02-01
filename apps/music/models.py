from django.db import models
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _

from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFit

from core.models import BaseModel, register_liked_model
from core.utils import time_int_to_str


class Album(SortableMixin, BaseModel):
    """Model for album information."""

    name = models.CharField(
        max_length=64,
        null=True,
        blank=False,
        verbose_name=_('Name'),
    )
    slug = models.CharField(
        blank=False,
        db_index=True,
        max_length=64,
        null=True,
        unique=True,
        verbose_name=_('Slug'),
    )
    year = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_('Year'),
    )
    status = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        verbose_name=_('Status'),
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
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(300, 300)],
        format='JPEG',
        options={'quality': 100},
    )
    description = models.TextField(
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
        return self.name or '-'

    class Meta:
        verbose_name = _('Album')
        verbose_name_plural = _('Albums')
        ordering = ('order',)

    @property
    def tracks_count(self) -> int:
        """Get count of all tracks in album."""
        return self.tracks.count()

    @property
    def duration(self) -> int:
        """Get summary album duration."""
        return sum(self.tracks.values_list('duration', flat=True))

    @property
    def displayed_duration(self) -> str:
        """Get summary album duration as MM:SS string."""
        return time_int_to_str(value=self.duration)


class AlbumFile(SortableMixin, BaseModel):
    """Model for files attached to album.

    For thinks like "download album as zip" links.
    """

    album = SortableForeignKey(
        Album,
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='album_files',
        verbose_name=_('Album'),
    )
    file = models.ForeignKey(
        'files.File',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='album_files',
        verbose_name=_('File'),
    )
    button_text = models.CharField(
        null=True,
        blank=False,
        max_length=255,
        verbose_name=_('Button text'),
    )
    button_class = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('Button class'),
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
        verbose_name=_('Order'),
    )

    def __str__(self):
        return f'{self.album} - {self.button_text} ({self.button_class})'

    class Meta:
        verbose_name = _('Album file')
        verbose_name_plural = _('Album files')
        ordering = ('order',)


@register_liked_model(name='music_track')
class Track(SortableMixin, BaseModel):
    """Model for storing track's information."""

    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Is active'),
    )
    album = SortableForeignKey(
        Album,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='tracks',
        verbose_name=_('Album'),
    )
    name = models.CharField(
        null=True,
        blank=False,
        max_length=255,
        verbose_name=_('Name'),
    )
    slug = models.CharField(
        blank=False,
        db_index=True,
        max_length=64,
        null=True,
        unique=True,
        verbose_name=_('Slug'),
    )
    file = models.ForeignKey(
        'files.File',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='tracks',
        verbose_name=_('File'),
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
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(200, 200)],
        format='JPEG',
        options={'quality': 80},
    )
    duration = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name=_('Duration'),
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
        verbose_name=_('Order'),
    )

    def __str__(self):
        return f'{self.album} - {self.name}'

    class Meta:
        verbose_name = _('Track')
        verbose_name_plural = _('Tracks')
        ordering = ('-order',)

    def save(self, *args, **kwargs):
        """Save model instance."""
        if not self.id:
            self.order = 0

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Get URL to specific track (for sitemap)."""
        return self.detail_url

    @property
    def music_files(self):
        """Get list of music files."""
        return self.related_files.filter(file__category__name='Музыка')

    @property
    def other_files(self):
        """Get list of other (not music) files."""
        return self.related_files.exclude(file__category__name='Музыка')

    @property
    def displayed_duration(self) -> str:
        """Get summary album duration as MM:SS string."""
        return time_int_to_str(value=self.duration)

    @property
    def detail_url(self):
        """Get detail url."""
        return reverse('music:detail', args=(self.album.slug,))

    @property
    def badge(self):
        return _('Track')


class TrackFile(SortableMixin, models.Model):
    """Intermediate model for M2M related between ``Track`` and ``File``."""

    track = models.ForeignKey(
        Track,
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='related_files',
        verbose_name=_('Track'),
    )
    file = models.ForeignKey(
        'files.File',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='related_tracks',
        verbose_name=_('File'),
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
        verbose_name=_('Order'),
    )

    def __str__(self):
        return self.file.name if self.file else '-'

    class Meta:
        verbose_name = _('Track file')
        verbose_name_plural = _('Track files')
        ordering = ('order',)


class MusicVideoType(SortableMixin, BaseModel):
    """Model for music video type."""

    name = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('Name'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
    )
    slug = models.CharField(
        blank=False,
        db_index=True,
        max_length=64,
        null=True,
        unique=True,
        verbose_name=_('Slug'),
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
        verbose_name = _('Music video type')
        verbose_name_plural = _('Music video types')
        ordering = ('order',)


class MusicVideo(BaseModel):
    """Model to music videos."""

    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Is active'),
    )
    video_type = models.ForeignKey(
        MusicVideoType,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='videos',
        verbose_name=_('Type'),
    )
    album = models.ForeignKey(
        Album,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='music_videos',
        verbose_name=_('Album'),
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('Name'),
    )
    slug = models.CharField(
        blank=False,
        db_index=True,
        max_length=64,
        null=True,
        unique=True,
        verbose_name=_('Slug'),
    )
    video = models.ForeignKey(
        'files.VideoFile',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='music_videos',
        verbose_name=_('Video'),
    )

    def __str__(self):
        return self.name or '-'

    class Meta:
        verbose_name = _('Music video')
        verbose_name_plural = _('Music videos')
        ordering = ('-created',)

    @property
    def thumbnail(self):
        """Get video image."""
        return self.video.poster_thumbnail if (self.video and self.video.poster) else None

    @property
    def link(self):
        """Get youtube video link."""
        return f'https://www.youtube.com/watch?v={self.video.youtube_link}'

    @property
    def detail_url(self):
        """Get detail url."""
        return self.link

    @property
    def badge(self):
        return _('Video')
