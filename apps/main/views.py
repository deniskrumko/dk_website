from django.db.models import Q
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import View

from core.views import BaseView

from apps.blog.models import BlogEntry
from apps.diary.models import DiaryEntry
from apps.music.models import Track
from apps.news.models import News

from .models import RedirectPage

__all__ = ('IndexView', 'RedirectView', 'SearchView', 'WakeMyDyno')


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
        context.update({
            'news_items': News.objects.all()[:3],
            'music_items': Track.objects.all()[:6],
            'total_news_count': News.objects.count()
        })
        return context


class RedirectView(View):
    """View to redirect pages."""

    def get(self, request, page=None):
        """Make redirect to provided page."""
        page = get_object_or_404(RedirectPage, source=page)
        return HttpResponseRedirect(page.destination)


class SearchView(BaseView):
    """View to search page."""

    template_name = 'search.html'
    title = 'DK - Поиск'
    description = 'Поиск данных на сайте deniskrumko.ru'
    menu = 'index'

    def find_music_tracks(self, search_query):
        """Find music tracks."""
        return Track.objects.filter(
            Q(name__icontains=search_query) |
            Q(short_description__icontains=search_query) |
            Q(full_description__icontains=search_query)
        ).distinct()

    def find_blog_entries(self, search_query):
        """Find blog entries."""
        return BlogEntry.objects.filter(
            Q(title__icontains=search_query) |
            Q(subtitle__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(text__icontains=search_query)
        ).distinct()

    def find_diary_entries(self, search_query):
        """Find diary entries."""
        return DiaryEntry.objects.filter(
            text__icontains=search_query
        ).distinct()

    def get(self, request, search_query=None):
        """Find object using search query."""
        form_search_query = request.GET.get('search_query')

        if not search_query and form_search_query:
            return HttpResponseRedirect(f'/search/{form_search_query}')

        context = self.get_context_data()

        results = {}

        MAX = 10

        # Fast way to go to admin page
        if search_query in ('ad', 'admin'):
            return HttpResponseRedirect('/admin')

        # Fast way to login/logout
        if search_query in ('login', 'logout'):
            return HttpResponseRedirect('/' + search_query)

        if search_query:
            tracks = self.find_music_tracks(search_query)

            if tracks:
                category = 'Музыка'
                if tracks.count() > MAX:
                    category += f' (Показано {MAX} из {tracks.count()})'

                results[category] = [
                    {
                        'title': track.name,
                        'preview': track.short_description[:100],
                        'url': f'/music/{track.slug}'
                    }
                    for track in tracks[:MAX]
                ]

            blogs = self.find_blog_entries(search_query)

            if blogs:
                category = 'Блоги'
                if blogs.count() > MAX:
                    category += f' (Показано {MAX} из {blogs.count()})'

                results[category] = [
                    {
                        'title': blog.title,
                        'preview': blog.subtitle,
                        'url': f'/blog/{blog.slug}'
                    }
                    for blog in blogs[:MAX]
                ]

            if request.user.is_superuser:
                diaries = self.find_diary_entries(search_query)

                if diaries:
                    category = 'Дневник'
                    if diaries.count() > MAX:
                        category += f' (Показано {MAX} из {diaries.count()})'

                    results[category] = [
                        {
                            'title': diary.date,
                            'preview': diary.text[:200] + '...',
                            'url': f'/diary/{diary.date}'
                        }
                        for diary in diaries[:MAX]
                    ]

        context['search_query'] = search_query
        context['categories'] = results

        return self.render_to_response(context)


class WakeMyDyno(View):
    """Text file response for staying always awake.

    Source: http://wakemydyno.com/

    """

    def get(self, request, page=None):
        """Send simple text to wake Heroku dyno."""
        content = "I'm worse at what I do best "
        return HttpResponse(content, content_type='text/plain')
