from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel


class DiaryEntry(BaseModel):
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

    @property
    def html(self):
        """Property to represent entry text as HTML."""
        text = self.text.replace('\r\n', '\n')
        return ''.join([
            f'<p>{line}</p>' if line else '<p>&nbsp;<p>'
            for line in text.split('\n')
        ])

    @property
    def preview(self):
        """Property to represent entry text as HTML (only preview)."""
        preview = ''
        for part in self.text.split('.'):
            if len(preview) > 120:
                return preview
            else:
                preview += f'{part}.'

        return self.text
