from django.core.management import BaseCommand

from apps.blog.factories import BlogEntryFactory
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
        # Music
        # ====================================================================

        dendynotdead = ArtistFactory(name='Dendy Not Dead')

        self.music_category = FileCategoryFactory(name='Музыка')
        self.gtp_category = FileCategoryFactory(name='GTP')

        for i in range(3):
            self.create_track(artist=dendynotdead)

        # Blog
        # ====================================================================

        BlogEntryFactory.create_batch(5)
        self.stdout.write(self.style.SUCCESS('\nCreated 5 blog entries'))

        self.stdout.write(self.style.SUCCESS(
            '\nDatabase successfully populated!'
        ))
