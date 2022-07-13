from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http.response import HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic.base import TemplateView

__all__ = (
    'BaseView',
    'LoginRequiredMixin',
)


class BaseView(TemplateView):
    """Base class for views."""

    menu = None
    title = None
    description = None
    use_analytics = False
    max_items_on_page = 10  # See `get_paginated_data()`

    def get_active_menu(self, **kwargs):
        """Get active menu item."""
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
        context_data['website_description'] = self.get_description(**kwargs)
        context_data['use_analytics'] = self.use_analytics
        return context_data

    def get_query_param(self, request, parameter, default=None):
        """Get query parameter."""
        return request.GET.get(parameter, default)

    def dispatch(self, request, *args, **kwargs):
        """Add user to view instance."""
        self.user = request.user
        return super().dispatch(request, *args, **kwargs)

    def redirect(self, url, use_reverse=True, args=None):
        """Make redirect to provided URL."""
        url = reverse(url, args=args) if use_reverse else url
        return HttpResponseRedirect(url)

    def get_paginated_data(self, items):
        """Get data for pagination."""
        paginator = Paginator(items, self.max_items_on_page)

        try:
            page = int(self.request.GET.get('page', 1))
            if not (1 < page <= paginator.num_pages):
                raise ValueError
        except Exception:
            page = 1

        current_page = paginator.page(page)
        return {
            'items': current_page.object_list,
            'paginator': paginator,
            'current_page': page,
            'prev_page': (
                current_page.previous_page_number()
                if current_page.has_previous()
                else None
            ),
            'next_page': (
                current_page.next_page_number()
                if current_page.has_next()
                else None
            ),
        }
