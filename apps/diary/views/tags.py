from django.shortcuts import get_object_or_404

from core.views import BaseView, LoginRequiredMixin

from ..models import DiaryTag


class DiaryTagsView(LoginRequiredMixin, BaseView):
    """View to get index page for diary tags."""

    template_name = 'diary/tags/index.html'
    title = 'DK - Тэги'
    description = 'Тэги дневника'
    menu = 'blog'

    def get_context_data(self):
        """Get context data."""
        context = super().get_context_data()
        context['available_tags'] = DiaryTag.objects.all()
        return context


class DiaryTagView(LoginRequiredMixin, BaseView):
    """View to get single tag info."""

    template_name = 'diary/tags/detail.html'
    menu = 'blog'

    def get_title(self, **kwargs):
        """Get `title` field value."""
        item = kwargs.get('item')
        return f'DK - #{item.name}' if item else ''

    def get_description(self, **kwargs):
        """Get `description` field value."""
        item = kwargs.get('item')
        return item.name if item else ''

    def get(self, request, tag):
        """Get tag details."""
        item = get_object_or_404(DiaryTag, name=tag)
        context = self.get_context_data(item=item)
        context['tag'] = item
        return self.render_to_response(context)
