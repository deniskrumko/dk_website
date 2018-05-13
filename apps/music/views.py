from core.views import BaseView
from .models import Artist


class TrackListView(BaseView):
    template_name = 'music/tracks_list.html'

    def get_context_data(self):
        return {
            'artists': Artist.objects.all()
        }
