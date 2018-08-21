from core.views import BaseView

from .models import BlogEntry


class BlogIndexView(BaseView):
    template_name = 'blog/index.html'
    menu = 'blog'
    title = 'DK - Блог'

    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'items': BlogEntry.objects.all(),
        })
        return context


class BlogDetailView(BaseView):
    template_name = 'blog/detail.html'
    menu = 'blog'

    def get_title(self, **kwargs):
        title = kwargs.get('title')
        return f'DK - {title}'

    def get(self, request, slug):

        item = BlogEntry.objects.filter(slug=slug).first()
        context = super().get_context_data(title=item.title)
        context.update({
            'item': item,
        })

        return self.render_to_response(context)
