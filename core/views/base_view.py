from django.views.generic.base import TemplateView


class BaseView(TemplateView):
    """Base class for views."""
    active_menu = None
    title = None

    def get_active_menu(self, **kwargs):
        return self.active_menu

    def get_title(self, **kwargs):
        return self.title

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_title(**kwargs)
        context_data['active_menu'] = self.get_active_menu(**kwargs)
        return context_data

    def get_query_param(self, request, parameter, default=None):
        return request.GET.get(parameter, default)
