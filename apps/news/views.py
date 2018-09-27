from .models import News
from core.views import BaseView


class NewsView(BaseView):
    """View for index page."""
    template_name = 'news.html'
    menu = 'index'
    title = 'DK - Новости'
    description = 'Новости сайта'
    use_analytics = True

    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'items': News.objects.all(),
        })
        return context
