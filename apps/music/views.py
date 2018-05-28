from core.views import BaseView
from .models import Track


class TrackListView(BaseView):
    template_name = 'music/track_list.html'

    def get_context_data(self):
        return {
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
        }


class TrackDetailsView(BaseView):
    template_name = 'music/track_details.html'

    def get(self, request, slug):

        track = Track.objects.filter(slug=slug).first()

        context = {
            'track': track,
            'music_files': track.related_files.filter(file__category__name='Музыка'),
            'other_files': track.related_files.exclude(file__category__name='Музыка')
        }

        return self.render_to_response(context)
