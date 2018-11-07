from django.shortcuts import get_object_or_404

from core.views import BaseView

from .models import Track


class TrackIndexView(BaseView):
    """View to get index tracks page."""

    template_name = 'music/index.html'
    menu = 'music'
    title = 'DK - Музыка'
    description = (
        'Dendy Not Dead — это музыкальный проект Дениса Крумко. Сам проект '
        'является собранием инструментальной рок музыки, составленной '
        'полностью в программе Guitar Pro, без записи живых инструментов. '
        'Проект создан для удобного хранения собственных музыкальных идей и '
        'не представляет из себя настоящую музыку.'
    )
    use_analytics = True

    def get_context_data(self):
        """Get context data."""
        context = super().get_context_data()
        context.update({
            'tracks': Track.objects.all(),
            'logo': [
                '1100100011001100101',
                '1010110010101010111',
                '1110011010101110010',
                '0000000000000000000',
                '0000110020200100000',
                '0000101000001110000',
                '0000101010100100000',
                '0000000000000000000',
                '0011001000011011000',
                '0010101100101010100',
                '0011100110111011100'
            ]
        })
        return context


class TrackDetailView(BaseView):
    """View to get detail info about track."""

    template_name = 'music/detail.html'
    menu = 'music'
    use_analytics = True

    def get_title(self, **kwargs):
        """Get `title` field value."""
        item = kwargs.get('item')
        return f'DK - {item.name}' if item else ''

    def get_description(self, **kwargs):
        """Get `description` field value."""
        item = kwargs.get('item')
        return item.short_description if item else ''

    def get(self, request, slug):
        """Get details for single track."""
        item = get_object_or_404(Track, slug=slug)
        context = self.get_context_data(item=item)
        context.update({'track': item})
        return self.render_to_response(context)
