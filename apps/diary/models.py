from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel


class DiaryEntry(BaseModel):
    """Model for single diary entry."""

    author = models.ForeignKey(
        'users.User',
        null=True,
        blank=False,
        related_name='diary_entries',
        on_delete=models.SET_NULL,
        verbose_name=_('Author'),
    )
    date = models.DateField(
        null=True,
        blank=False,
        verbose_name=_('Date'),
    )
    text = models.TextField(
        null=True,
        blank=False,
        verbose_name=_('Text'),
    )
    done = models.BooleanField(
        default=False,
        verbose_name=_('done'),
    )
    files = models.ManyToManyField(
        'files.File',
        blank=True,
        related_name='diary_entries',
        verbose_name=_('files'),
    )

    class Meta:
        verbose_name = _('Diary entry')
        verbose_name_plural = _('Diary entries')
        ordering = ('-date',)

    def __str__(self):
        return f'{self.date} ({self.author.username})'

    @property
    def html(self):
        """Represent entry text as HTML."""
        def add_link(line):
            first_word = line.split()[0]

            if first_word.startswith('#'):
                link = (
                    f'<a href="/diary/tags/{first_word[1:]}" '
                    f'class="dk-a">{first_word}</a>'
                )
                line = line.replace(first_word, link)

            return line

        text = self.text.replace('\r\n', '\n')
        return ''.join([
            f'<p>{add_link(line)}</p>' if line else '<p>&nbsp;<p>'
            for line in text.split('\n')
        ])

    @property
    def preview(self):
        """Represent entry text as HTML (only preview)."""
        preview = ''
        for part in self.text.split('.'):
            if len(preview) > 120:
                return preview
            else:
                preview += f'{part}.'

        return self.text

    def populate_tags(self, delete_tags=True):
        """Add tags for current instance."""
        if not self.author:
            return

        if delete_tags:
            self.tags.filter(author=self.author).delete()

        for line in self.text.split('\n'):
            line = line.strip()

            if line.startswith('#'):

                tag_name, *other = line.split()

                tag, created = DiaryTag.objects.get_or_create(
                    name=tag_name[1:],
                    author=self.author,
                )

                DiaryTagValue.objects.create(
                    tag=tag,
                    author=self.author,
                    entry=self,
                    value=' '.join(other) if other else None
                )


class DiaryTag(BaseModel):
    """Model for tags in diary entries."""

    name = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('name'),
    )
    author = models.ForeignKey(
        'users.User',
        null=True,
        blank=False,
        related_name='diary_tags',
        on_delete=models.SET_NULL,
        verbose_name=_('Author'),
    )
    entries = models.ManyToManyField(
        'diary.DiaryEntry',
        through='diary.DiaryTagValue',
        blank=True,
        verbose_name=_('entries'),
    )

    def __str__(self):
        return self.name or '-'

    class Meta:
        verbose_name = _('Diary tag')
        verbose_name_plural = _('Diary tags')
        ordering = ('name',)

    @property
    def ordered_entries(self):
        """Get queryset of ordered by date tag values."""
        return self.values.order_by('-entry__date')


class DiaryTagValue(BaseModel):
    """Model for value of tag for specific entry."""

    tag = models.ForeignKey(
        'diary.DiaryTag',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='values',
        verbose_name=_('tag'),
    )
    author = models.ForeignKey(
        'users.User',
        null=True,
        blank=False,
        related_name='diary_tag_values',
        on_delete=models.SET_NULL,
        verbose_name=_('Author'),
    )
    entry = models.ForeignKey(
        'diary.DiaryEntry',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='tags',
        verbose_name=_('entry'),
    )
    value = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('value'),
    )

    def __str__(self):
        return f'{self.tag}: {self.value}'

    class Meta:
        verbose_name = _('Diary tag value')
        verbose_name_plural = _('Diary tag values')
        ordering = ('tag__name', 'value')
