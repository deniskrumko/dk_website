from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import View

from core.views import BaseView

from apps.news.models import News

from .models import RedirectPage

__all__ = ('IndexView', 'RedirectView')


class IndexView(BaseView):
    """View for index page."""
    template_name = 'index.html'
    menu = 'index'
    title = 'Denis Krumko'
    description = (
        'Сайт Дениса Крумко: видеоблоги о путешествиях, инструментальная '
        'музыка, ну и все. Смотрите, слушайте, узнавайте.'
    )
    use_analytics = True

    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'news_items': News.objects.all()[:4],
            'total_news_count': News.objects.count()
        })
        return context


class RedirectView(View):
    """View to redirect pages."""

    def get(self, request, page=None):
        page = get_object_or_404(RedirectPage, source=page)
        return HttpResponseRedirect(page.destination)
