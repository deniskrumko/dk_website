from django.shortcuts import get_object_or_404

from core.views import BaseView

from .models import BlogEntry


class BlogIndexView(BaseView):
    """View to get index blogs page."""
    template_name = 'blog/index.html'
    menu = 'blog'
    title = 'DK - Блог'
    description = (
        'Блог Дениса Крумко: видео о путешествиях за границу и '
        'на различные музыкальные концерты. Много музыки и много видео :)'
    )
    use_analytics = True

    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'items': BlogEntry.objects.filter(is_active=True),
        })
        return context


class BlogDetailView(BaseView):
    """View to get details about blog entry."""
    template_name = 'blog/detail.html'
    menu = 'blog'
    use_analytics = True

    def get_title(self, **kwargs):
        item = kwargs.get('item')
        return f'DK - {item.title}' if item else ''

    def get_description(self, **kwargs):
        item = kwargs.get('item')
        return item.description if item else ''

    def get(self, request, slug):
        item = get_object_or_404(BlogEntry, slug=slug)
        context = self.get_context_data(item=item)
        context.update({
            'item': item,
            'degrees': list(range(-15, 15)),
        })
        return self.render_to_response(context)


class BlogDownloadView(BaseView):
    """View to get download blog entry video."""
    template_name = 'blog/download.html'
    menu = 'blog'
    use_analytics = True

    def get_title(self, **kwargs):
        item = kwargs.get('item')
        return f'DK - {item.title} - Скачать' if item else ''

    def get_description(self, **kwargs):
        item = kwargs.get('item')
        return item.description if item else ''

    def get(self, request, slug):
        item = get_object_or_404(BlogEntry, slug=slug)
        context = self.get_context_data(item=item)
        context.update({'item': item})
        return self.render_to_response(context)
