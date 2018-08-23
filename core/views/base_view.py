from django.views.generic.base import TemplateView

from apps.main.menu import get_menu


class BaseView(TemplateView):
    """Base class for views."""
    menu = None
    title = None

    def get_active_menu(self, **kwargs):
        assert self.menu, 'Add `menu` to {}'.format(self.__class__)
        return self.menu

    def get_title(self, **kwargs):
        assert self.title, 'Add `title` to {}'.format(self.__class__)
        return self.title

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_title(**kwargs)
        context_data['active_menu'] = self.get_active_menu(**kwargs)
        context_data['menu'] = get_menu()
        return context_data

    def get_query_param(self, request, parameter, default=None):
        return request.GET.get(parameter, default)