import calendar
from datetime import date, datetime, timedelta

from django.conf import settings
from django.core.exceptions import ValidationError
from django.http.response import HttpResponseRedirect
from django.shortcuts import reverse
from django.utils import timezone

from cachetools import TTLCache, cached
from dateutil.rrule import DAILY, rrule

from core.views import BaseView, LoginRequiredMixin

from apps.files.models import File, FileCategory

from ..models import DiaryEntry, DiaryTag

__all__ = (
    'DiaryDetailView',
    'DiaryEditView',
    'DiaryFileUploadView',
    'DiaryIndexView',
    'DiarySearchView',
)


class BaseDiaryView(LoginRequiredMixin, BaseView):
    """Base class for diary-related views."""

    DATE_FORMAT = '%Y-%m-%d'
    menu = 'diary'
    description = 'Дневник'
    colors = ('#00ACC1', '#0795a6', '#f9f9f9')

    @property
    @cached(cache=TTLCache(maxsize=128, ttl=60))
    def now(self):
        return timezone.now()

    @property
    def now_str(self):
        return self.now.strftime(self.DATE_FORMAT)

    def get_month_bounds(self, dt):
        last_day = calendar.monthrange(dt.year, dt.month)[1]
        return date(dt.year, dt.month, 1), date(dt.year, dt.month, last_day)

    def get_month_links(self, dt):
        first_day, last_day = self.get_month_bounds(dt)
        prev_month = (first_day - timedelta(days=1)).replace(day=1)
        next_month = (last_day + timedelta(days=1))

        if (
            prev_month.year == self.now.year
            and prev_month.month == self.now.month
        ):
            prev_month = self.now.date()

        if (
            next_month.year == self.now.year
            and next_month.month == self.now.month
        ):
            next_month = self.now.date()

        return prev_month, next_month


class DiaryIndexView(BaseDiaryView):
    """View to get index diary page."""

    def get(self, request):
        """Redirect to current date page."""
        return self.redirect('diary:detail', args=(self.now_str,))


class DiaryDetailView(BaseDiaryView):
    """Detail view for diary entries."""

    template_name = 'diary/detail.html'

    def get(self, request, date):
        """Get single entry."""
        try:
            entry = DiaryEntry.objects.filter(
                author=self.user,
                date=date,
            ).first()
        except ValidationError:
            # Incorrect date format
            return self.redirect('diary:index')

        dt = datetime.strptime(date, self.DATE_FORMAT)
        context = self.get_context_data(dt=dt)

        try:
            years_range = 1
            jump_to_year = [
                (dt.year - i, dt.date().replace(year=(dt.year - i)),)
                for i in range(years_range, -years_range - 1, -1) if i != 0
            ]
        except Exception:
            # This happened for February 29
            jump_to_year = []

        context.update({
            'dt': dt,
            'entry': entry,
            'tags': DiaryTag.objects.filter(author=self.user),
            'month': self.get_month_data(dt),
            'current': self.now,
            # TODO: Move to template later ---
            'detail_link': reverse('diary:detail', args=(date,)),
            'edit_link': reverse('diary:edit', args=(date,)),
            'file_link': reverse('diary:file_upload', args=(date,)),
            # --------------------------------
            'month_links': self.get_month_links(dt),
            'next_day': (dt + timedelta(days=1)).date(),
            'prev_day': (dt - timedelta(days=1)).date(),
            'next_week': (dt + timedelta(days=7)).date(),
            'prev_week': (dt - timedelta(days=7)).date(),
            'jump_to_year': jump_to_year,
        })
        return self.render_to_response(context)

    def get_title(self, **kwargs):
        """Get `title` field value."""
        return f'DK - Дневник ({kwargs["dt"].strftime("%d.%m.%Y")})'

    def get_month_data(self, dt):
        first_day, last_day = self.get_month_bounds(dt)
        done_dates = DiaryEntry.objects.filter(
            author=self.user,
            done=True,
            date__gte=first_day,
            date__lte=last_day,
        ).values_list('date', flat=True)

        month = []

        for date_obj in rrule(DAILY, dtstart=first_day, until=last_day):
            if date_obj.day == 1:
                for i in range(date_obj.weekday()):
                    month.append({'date': '-', 'classes': 'empty'})

            classes = []

            if date_obj.date() not in done_dates:
                if date_obj.date() < self.now.date():
                    classes.append('critical')

            if date_obj.date() == dt.date():
                classes.append('primary')

            if date_obj.date() == self.now.date():
                classes.append('bold')

            month.append({
                'date': date_obj.date(),
                'classes': ' '.join(classes),
            })

        return month


class DiaryEditView(DiaryDetailView):
    """View to edit single diary entry."""

    template_name = 'diary/edit.html'

    def post(self, request, date):
        """Get updated entry."""
        text = request.POST.get('text')
        done = bool(request.POST.get('done') == 'on')

        DiaryEntry.objects.update_or_create(
            author=self.user,
            date=date,
            defaults={
                'text': text,
                'done': done
            }
        )

        return HttpResponseRedirect(reverse('diary:detail', args=(date,)))


class DiaryFileUploadView(BaseDiaryView):
    """View to upload file to diary entry."""

    template_name = 'diary/file_upload.html'
    title = 'DK - Загрузка файла'

    def get(self, request, date, errors=None):
        """Get single entry."""
        context = self.get_context_data()
        context.update({
            'form_url': reverse('diary:file_upload', args=(date,)),
            'back_url': reverse('diary:detail', args=(date,)),
            'file_categories': FileCategory.objects.all(),
            'errors': errors,
        })
        return self.render_to_response(context)

    def post(self, request, date):
        """Get updated entry."""
        errors = []
        name = request.POST.get('name')
        if not name:
            errors.append('Укажите название файла')

        category = request.POST.get('category')

        uploaded_file = request.FILES.get('file')
        if not uploaded_file:
            errors.append('Загрузите файл')

        if errors:
            return self.get(request, date, errors=errors)

        entry, created = DiaryEntry.objects.get_or_create(
            author=self.user,
            date=date,
            defaults={'text': ''}
        )
        new_file = File.objects.create(
            name=name,
            data=uploaded_file,
            category_id=category,
        )
        entry.files.add(new_file)

        return HttpResponseRedirect(reverse('diary:detail', args=(date,)))


class DiarySearchView(BaseDiaryView):

    template_name = 'diary/search.html'
    title = 'DK - Поиск в дневнике'

    def get(self, request, month=None, year=None, query=''):
        """Get single entry."""
        context = self.get_context_data()

        month = month or self.now.month
        year = year or self.now.year
        start_month = month if month != 13 else 1
        end_month = month if month != 13 else 12

        last_day_of_month = calendar.monthrange(year, end_month)[1]
        qs = DiaryEntry.objects.filter(author=self.user)

        if query:
            qs = qs.filter(text__icontains=query)
            context['found_amount'] = qs.count()
            days = [
                (item.date, item) for item in qs
            ]
        else:
            days = []
            for dt in rrule(
                DAILY,
                dtstart=date(year, start_month, 1),
                until=date(year, end_month, last_day_of_month)
            ):
                cur_date = dt.date()
                cur_entry = qs.filter(date=cur_date).first()
                days.append((cur_date, cur_entry))

        context.update({
            'entries': days,
            'query': query,
            'months': settings.MONTH_LIST,
            'years': self.years,
            'selected_month': month,
            'selected_month_name': (
                settings.MONTH_LIST[month - 1] if month < 13 else ''
            ),
            'selected_year': year,
        })
        return self.render_to_response(context)

    def post(self, request):
        month = int(request.POST.get('month', 0))
        year = int(request.POST.get('year', 0))
        query = request.POST.get('query')
        return self.get(request, month=month, year=year, query=query)

    @property
    def years(self):
        year = self.now.year
        while year != 2015:
            yield year
            year -= 1
