from django.shortcuts import get_object_or_404

from core.views import BaseView

from .models import Album, MusicVideoType, Track


class MusicIndexView(BaseView):
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
        context['albums'] = Album.objects.all()
        return context


class AlbumDetailView(BaseView):
    """View to get detail info about album."""

    template_name = 'music/album.html'
    menu = 'music'
    use_analytics = True

    def get_title(self, **kwargs):
        """Get `title` field value."""
        album = kwargs.get('album')
        return f'DK - {album.name}' if album else ''

    def get_description(self, **kwargs):
        """Get `description` field value."""
        album = kwargs.get('album')
        return f'Альбом {album.name}'

    def get(self, request, slug):
        """Get details for single album."""
        album = get_object_or_404(Album, slug=slug)
        context = self.get_context_data(album=album)
        context.update({'album': album})
        return self.render_to_response(context)


class TracksView(BaseView):
    """View to get all available tracks."""

    template_name = 'music/tracks.html'
    menu = 'music'
    title = 'DK - Музыка'
    description = 'Все треки'
    use_analytics = True

    def get(self, request):
        """Get all tracks."""
        context = self.get_context_data()
        context.update({'tracks': Track.objects.order_by('album', '-order')})
        return self.render_to_response(context)


class MusicVideoView(BaseView):
    """View to get all music videos."""

    template_name = 'music/videos.html'
    menu = 'music'
    title = 'DK - Музыка'
    description = 'Музыкальные видео'
    use_analytics = True

    def get(self, request):
        """Get all videos."""
        context = self.get_context_data()
        context.update({'video_types': MusicVideoType.objects.all()})
        return self.render_to_response(context)
