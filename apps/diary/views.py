from datetime import date, datetime, timedelta

from django.http.response import Http404, HttpResponseRedirect
from django.utils import timezone

from dateutil import relativedelta
from dateutil.rrule import DAILY, rrule

from core.views import BaseView

from .models import DiaryEntry

__all__ = ('DiaryIndexView', 'DiaryDetailView', 'DiaryEditView')


class DiaryIndexView(BaseView):
    template_name = 'diary/index.html'
    menu = 'diary'

    def get(self, request):

        current_year = timezone.now().year
        current_month = timezone.now().month
        current_day = timezone.now().day

        a = date(current_year, current_month, 1)
        b = a + relativedelta.relativedelta(months=1) - relativedelta.relativedelta(days=1)

        days = []
        for dt in rrule(DAILY, dtstart=a, until=b):

            if dt.day == 1:
                for i in range(dt.weekday()):
                    days.append('-')

            days.append(
                (dt.date(), True)
            )

        context = self.get_context_data()

        context.update({
            'entries': DiaryEntry.objects.all(),
            'days': days,
            'current_day': current_day,
        })
        return self.render_to_response(context)


class DiaryDetailView(BaseView):
    template_name = 'diary/item.html'

    def get(self, request):
        context = {
            'entry': DiaryEntry.objects.first(),
        }
        return self.render_to_response(context)


class DiaryEditView(BaseView):
    template_name = 'diary/edit.html'

    def get(self, request):
        context = {
            'entry': DiaryEntry.objects.first(),
        }
        return self.render_to_response(context)

    def post(self, request, date=None):
        text = request.POST.get('text')

        d = DiaryEntry.objects.first()
        d.text = text
        d.save()

        # DiaryEntry.objects.update_or_create(
        #     author=request.user,
        #     date=date,
        #     defaults={
        #         'text': text
        #     }
        # )

        # messages.add_message(
        #     request, messages.SUCCESS, 'Дневник успешно сохранен!'
        # )

        return HttpResponseRedirect(f'/blog/diary/entry')
