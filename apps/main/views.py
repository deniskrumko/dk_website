from core.views import BaseView

__all__ = ('IndexView',)


class IndexView(BaseView):
    """View for index page."""
    template_name = 'index.html'
    menu = 'index'
    title = 'DK - Главная'
