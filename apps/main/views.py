from core.views import BaseView

from apps.news.models import News

__all__ = ('IndexView',)


class IndexView(BaseView):
    """View for index page."""
    template_name = 'index.html'
    menu = 'index'
    title = 'DK - Главная'

    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'news_items': News.objects.all(),
        })
        return context
