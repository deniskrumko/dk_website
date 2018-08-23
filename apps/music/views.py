from core.views import BaseView

from .models import Track


class TrackIndexView(BaseView):
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

    def get_context_data(self):
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
                '00111001101110111000'
            ]
        })
        return context


class TrackDetailView(BaseView):
    template_name = 'music/detail.html'
    menu = 'music'

    def get_title(self, **kwargs):
        name = kwargs.get('track_name')
        return f'DK - {name}'

    def get_description(self, **kwargs):
        return kwargs.get('track_description')

    def get(self, request, slug):

        track = Track.objects.filter(slug=slug).first()
        context = super().get_context_data(
            track_name=track.name,
            track_description=track.short_description
        )
        context.update({
            'track': track,
            'music_files': track.related_files.filter(
                file__category__name='Музыка'
            ),
            'other_files': track.related_files.exclude(
                file__category__name='Музыка'
            )
        })

        return self.render_to_response(context)
