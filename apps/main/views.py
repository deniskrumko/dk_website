from django.http.response import Http404, HttpResponseRedirect
from django.views import View

from core.views import BaseView

from apps.news.models import News

from .models import RedirectPage

__all__ = ('IndexView', 'RedirectView')


class IndexView(BaseView):
    """View for index page."""
    template_name = 'index.html'
    menu = 'index'
    title = 'DK - Главная'
    description = 'Сайт Дениса Крумко: видео, музыка и все такое'

    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'news_items': News.objects.all(),
        })
        return context


class RedirectView(View):

    def get(self, request, page=None):
        page = RedirectPage.objects.filter(source=page).first()

        if not page:
            raise Http404

        return HttpResponseRedirect(page.destination)
