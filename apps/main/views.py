from django.http.response import Http404, HttpResponseRedirect, JsonResponse
from django.views import View

from core.models import LIKED_MODELS_REGISTRY
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


class LikesView(View):

    def error_response(self):
        return JsonResponse(data={'result': ''})

    def post(self, request, obj_name=None, obj_id=None):
        model_class = LIKED_MODELS_REGISTRY.get(obj_name)

        if not model_class:
            return self.error_response()

        obj = model_class.objects.filter(id=obj_id).first()

        if not obj:
            return self.error_response()

        return JsonResponse(data={'result': obj.increment_likes()})
