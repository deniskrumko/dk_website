from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

from apps.main.menu import get_hidden_menu, get_menu

__all__ = ('BaseView', 'LoginRequiredMixin')


class BaseView(TemplateView):
    """Base class for views."""

    menu = None
    title = None
    description = None
    use_analytics = False

    def get_active_menu(self, **kwargs):
        """Get active menu item."""
        assert self.menu, 'Add `menu` to {}'.format(self.__class__)
        return self.menu

    def get_title(self, **kwargs):
        """Get `title` field value."""
        assert self.title, 'Add `title` to {}'.format(self.__class__)
        return self.title

    def get_description(self, **kwargs):
        """Get `description` field value."""
        assert self.description, \
            'Add `description` to {}'.format(self.__class__)
        return self.description

    def get_context_data(self, **kwargs):
        """Get context data."""
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_title(**kwargs)
        context_data['active_menu'] = self.get_active_menu(**kwargs)
        context_data['menu'] = get_menu()
        context_data['hidden_menu'] = get_hidden_menu()
        context_data['website_description'] = self.get_description(**kwargs)
        context_data['use_analytics'] = self.use_analytics
        return context_data

    def get_query_param(self, request, parameter, default=None):
        """Get query parameter."""
        return request.GET.get(parameter, default)
