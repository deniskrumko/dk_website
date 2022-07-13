from django.shortcuts import get_object_or_404

from core.views import BaseView

from .models import BlogCategory, BlogEntry


class BaseBlogView(BaseView):
    """Base class for blog-related views."""

    menu = 'video'


class BlogIndexView(BaseBlogView):
    """View to get index blogs page."""

    template_name = 'blog/index.html'
    queryset = BlogEntry.objects.filter(is_active=True)
    max_items_on_page = 12
    title = 'DK - Видео'
    description = (
        'DK: видео о путешествиях за границу и '
        'на различные музыкальные концерты. Много музыки и много видео :)'
    )
    use_analytics = True

    def get(self, request):
        category = request.GET.get('category')
        context = self.get_context_data(category)
        return self.render_to_response(context)

    def get_queryset(self, category: str):
        if category and BlogCategory.objects.filter(slug=category).exists():
            return self.queryset.filter(category__slug=category)

        return self.queryset

    def get_context_data(self, category: str = None):
        """Get context data."""
        context = super().get_context_data()
        queryset = self.get_queryset(category)
        context.update(self.get_paginated_data(items=queryset))

        context['categories'] = BlogCategory.objects.all()
        context['current_category'] = category
        return context


class BlogDetailView(BaseBlogView):
    """View to get details about blog entry."""

    template_name = 'blog/detail.html'
    use_analytics = True

    def get_title(self, **kwargs):
        """Get `title` field value."""
        item = kwargs.get('item')
        return f'DK - {item.title}' if item else ''

    def get_description(self, **kwargs):
        """Get `description` field value."""
        item = kwargs.get('item')
        return item.description if item else ''

    def get(self, request, slug):
        """Get blog details."""
        item = get_object_or_404(BlogEntry, slug=slug)
        context = self.get_context_data(item=item)
        mapping = {
            '360p': item.video.source_360,
            '480p': item.video.source_480,
            '720p': item.video.source_720,
            '1080p': item.video.source_1080,
        } if item.video else {}
        quality = self.request.GET.get('quality')
        current_page = self.request.GET.get('page')
        if quality not in mapping:
            quality = '720p'

        context.update({
            'item': item,
            'video_src': mapping.get(quality),
            'quality': quality,
            'current_page': current_page,
            'available_quality': filter(lambda x: mapping[x], mapping.keys()),
        })
        return self.render_to_response(context)


class AboutProjectView(BaseBlogView):
    """View to get info about project."""

    template_name = 'blog/about.html'
    title = 'DK - О проекте'
    description = 'Кратко и по делу'
