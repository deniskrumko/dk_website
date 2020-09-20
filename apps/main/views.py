from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View

from core.views import BaseView

from apps.blog.models import BlogEntry
from apps.music.models import MusicVideo, Track

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
        blog_qs = BlogEntry.objects.filter(is_active=True)
        music_items = sorted([
            *list(Track.objects.order_by('-created')[:8]),
            *list(MusicVideo.objects.all()[:8]),
        ], key=lambda x: -x.created.timestamp())
        context.update({
            'blog_items': blog_qs[:5],
            'music_items': music_items[:8],
            'total_blog_items': blog_qs.count() - 5,
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
