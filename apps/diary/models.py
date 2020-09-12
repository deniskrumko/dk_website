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
        verbose_name=_('Done'),
    )
    files = models.ManyToManyField(
        'files.File',
        blank=True,
        related_name='diary_entries',
        verbose_name=_('Files'),
    )

    class Meta:
        verbose_name = _('Diary entry')
        verbose_name_plural = _('Diary entries')
        ordering = ('-date',)

    def __str__(self):
        author = self.author.username if self.author else 'unknown'
        return f'{self.date} ({author})'

    @property
    def html(self):
        """Represent entry text as HTML."""
        def add_link(line):
            parts = line.split()
            if not parts:
                return line

            first_word = parts[0]
            if first_word.startswith('#'):
                link = (
                    f'<a href="/diary/tags/{first_word[1:]}" '
                    f'class="dk-a">{first_word}</a>'
                )
                line = line.replace(first_word, link)

            return line

        try:
            text = self.text.replace('\r\n', '\n')
            return ''.join([
                f'<p>{add_link(line)}</p>' if line else '<p>&nbsp;<p>'
                for line in text.split('\n')
            ])
        except Exception as e:
            return f'Ошибка получения HTML: {e!r}'

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
        if not self.author or not self.text:
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
                    value=' '.join(other) if other else None,
                )

        # Remove unused tags
        for tag in DiaryTag.objects.filter(author=self.author):
            if not tag.values.exists():
                tag.delete()


class DiaryTag(BaseModel):
    """Model for tags in diary entries."""

    name = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('Name'),
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
        verbose_name=_('Entries'),
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

    @property
    def entries_count(self):
        count = self.values.count()
        word = 'записей'
        if count == 1:
            word = 'запись'
        elif str(count)[-1] in ('2', '3', '4'):
            word = 'записи'
        return f'{count} {word}'


class DiaryTagValue(BaseModel):
    """Model for value of tag for specific entry."""

    tag = models.ForeignKey(
        'diary.DiaryTag',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='values',
        verbose_name=_('Tag'),
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
        verbose_name=_('Entry'),
    )
    value = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Value'),
    )

    def __str__(self):
        return f'{self.tag}: {self.value}'

    class Meta:
        verbose_name = _('Diary tag value')
        verbose_name_plural = _('Diary tag values')
        ordering = ('tag__name', 'value')
