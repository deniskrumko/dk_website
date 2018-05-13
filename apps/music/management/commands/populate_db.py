from django.core.management import BaseCommand

from apps.files.factories import FileCategoryFactory, FileFactory
from apps.music.factories import ArtistFactory, TrackFactory, TrackFileFactory


class Command(BaseCommand):
    """Command to populate database with test data."""

    def create_track(self, artist):
        music_file = FileFactory(category=self.music_category)
        gtp_file = FileFactory(category=self.gtp_category)
        track = TrackFactory(artist=artist, file=music_file)
        TrackFileFactory(track=track, file=music_file)
        TrackFileFactory(track=track, file=gtp_file)
        self.stdout.write(self.style.SUCCESS(f'{artist.name} - {track.name}'))

    def handle(self, *args, **options):
        dendynotdead = ArtistFactory(name='Dendy Not Dead')
        deniskrumko = ArtistFactory(name='Denis Krumko')

        self.music_category = FileCategoryFactory(name='Музыка')
        self.gtp_category = FileCategoryFactory(name='GTP')

        for i in range(10):
            self.create_track(artist=dendynotdead)

        for i in range(10):
            self.create_track(artist=deniskrumko)

        self.stdout.write(self.style.SUCCESS(
            '\nDatabase successfully populated!'
        ))
