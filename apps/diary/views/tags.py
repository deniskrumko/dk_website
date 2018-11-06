import calendar
from datetime import date, timedelta
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import reverse
from django.utils import timezone

from dateutil.rrule import DAILY, rrule

from core.views import BaseView

from ..models import DiaryEntry, DiaryTag


class DiaryTagsView(LoginRequiredMixin, BaseView):
    """View to get index diary page."""

    template_name = 'diary/tags/index.html'
    title = 'DK - Дневник'
    description = 'Дневник'
    menu = 'blog'

    def get_context_data(self):
        context = super().get_context_data()
        context['available_tags'] = DiaryTag.objects.all()
        return context


class DiaryTagView(LoginRequiredMixin, BaseView):
    """View to get index diary page."""

    template_name = 'diary/tags/detail.html'
    title = 'DK - Дневник'
    description = 'Дневник'
    menu = 'blog'

    def get(self, request, tag):
        context = self.get_context_data()
        context['tag'] = get_object_or_404(DiaryTag, name=tag)
        return self.render_to_response(context)
