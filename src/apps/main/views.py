from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View

from core.views import BaseView

from apps.blog.models import BlogEntry
from apps.music.models import Album, MusicVideo

from .models import RedirectPage

__all__ = (
    'IndexView',
    'RedirectView',
    'WakeMyDyno',
)


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
        """Get context data."""
        context = super().get_context_data()
        last_video = BlogEntry.objects.filter(is_active=True).first()
        last_album = Album.objects.first()
        last_rep = MusicVideo.objects.filter(video_type__name='Репетиции')[:4]
        context.update({
            'last_video': last_video,
            'last_album': last_album,
            'last_rep': last_rep,
        })
        return context


class RedirectView(View):
    """View to redirect pages."""

    def get(self, request, page=None):
        """Make redirect to provided page."""
        page = get_object_or_404(RedirectPage, source=page)
        return HttpResponseRedirect(page.destination)


class WakeMyDyno(View):
    """Text file response for staying always awake.

    Source: http://wakemydyno.com/

    """

    def get(self, request, page=None):
        """Send simple text to wake Heroku dyno."""
        content = "I'm worse at what I do best."
        return HttpResponse(content, content_type='text/plain')


def http_404_view(request, *args, **kwargs):
    """View for HTTP 404 page."""
    response = render(request, "system/404.html", {})
    response.status_code = 404
    return response
