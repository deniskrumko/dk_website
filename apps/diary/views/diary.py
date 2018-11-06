import calendar
from datetime import date, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import reverse
from django.utils import timezone

from dateutil.rrule import DAILY, rrule

from core.views import BaseView

from ..models import DiaryEntry, DiaryTag

__all__ = (
    'DiaryIndexView',
    'DiaryDetailView',
    'DiaryCalendarView',
    'DiaryEditView',
)

DATE_FORMAT = '%Y-%m-%d'


class DiaryIndexView(BaseView):
    """View to get index diary page."""

    template_name = 'diary/index.html'
    title = 'DK - Дневник'
    description = 'Дневник'
    menu = 'blog'

    def get(self, request):
        """Get index page."""
        context = self.get_context_data()

        if not request.user.is_superuser:
            return self.render_to_response(context)

        current = timezone.now()

        last_day_of_month = calendar.monthrange(current.year, current.month)[1]

        existing_entries = {
            entry.date: True if entry.date else False
            for entry in DiaryEntry.objects.filter(
                author=request.user,
                done=True
            )
        }

        days = []
        for dt in rrule(
            DAILY,
            dtstart=date(current.year, current.month, 1),
            until=date(current.year, current.month, last_day_of_month)
        ):
            if dt.day == 1:
                for i in range(dt.weekday()):
                    days.append('-')

            days.append(
                (dt.date(), existing_entries.get(dt.date(), False))
            )

        for i in range(7 - dt.weekday()):
            days.append('-')

        last_days = [
            current - timezone.timedelta(days=i)
            for i in range(0, 6)
        ]

        for index, d in enumerate(last_days):
            last_days[index] = {
                'day': d,
                'entry': DiaryEntry.objects.filter(
                    date=d, author=self.request.user
                ).first()
            }

        context.update({
            'entries': DiaryEntry.objects.all(),
            'days': days,
            'current': current,
            'last_days': last_days,
        })
        return self.render_to_response(context)


class DiaryCalendarView(LoginRequiredMixin, BaseView):
    """View for calendar page on diary."""

    template_name = 'diary/calendar.html'
    menu = 'blog'
    title = 'DK - Календарь'
    description = 'Дневник'

    def get(self, request):
        """Get calendar page."""
        context = self.get_context_data()
        current = timezone.now()
        context['months'] = [
            timezone.datetime(year=1993, month=i, day=1) for i in range(1, 13)
        ]
        context['years'] = [
            current.year - i
            for i in range(0, 20)
        ]
        return self.render_to_response(context)


class DiaryDetailView(LoginRequiredMixin, BaseView):
    """Detail view for diary entries."""

    template_name = 'diary/detail.html'
    menu = 'blog'
    description = 'Дневник'

    def get_title(self):
        """Get `title` field value."""
        return f'DK - {self.date_obj.strftime("%d.%m.%Y")}'

    def get_entry(self, date, author):
        """Get `entry` field value."""
        return DiaryEntry.objects.filter(author=author, date=date).first()

    def get(self, request, date):
        """Get single entry."""
        self.date_obj = timezone.datetime.strptime(date, DATE_FORMAT)
        self.entry = self.get_entry(date=date, author=request.user)

        context = self.get_context_data()
        context['entry'] = self.entry
        context['date_str'] = date
        context['date_obj'] = self.date_obj
        context['prev_date'] = self.date_obj - timedelta(days=1)
        context['next_date'] = self.date_obj + timedelta(days=1)
        context['available_tags'] = DiaryTag.objects.all()
        return self.render_to_response(context)


class DiaryEditView(DiaryDetailView):
    """View to edit single diary entry."""

    template_name = 'diary/edit.html'
    menu = 'blog'
    description = 'Дневник'

    def post(self, request, date):
        """Get updated entry."""
        text = request.POST.get('text')
        done = bool(request.POST.get('done'))

        DiaryEntry.objects.update_or_create(
            author=request.user,
            date=date,
            defaults={
                'text': text,
                'done': done
            }
        )

        return HttpResponseRedirect(reverse('diary:detail', args=(date,)))