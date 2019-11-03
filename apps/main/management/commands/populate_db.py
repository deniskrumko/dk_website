from django.core.management import BaseCommand

from apps.blog.factories import (
    BlogEntryFactory,
    BlogSeriesFactory,
    BlogSeriesItemFactory,
)
from apps.files.factories import FileCategoryFactory, FileFactory
from apps.music.factories import AlbumFactory, TrackFactory, TrackFileFactory


class Command(BaseCommand):
    """Command to populate database with test data."""

    def create_track(self, album):
        """Create ``Track``."""
        music_file = FileFactory(category=self.music_category)
        gtp_file = FileFactory(category=self.gtp_category)
        track = TrackFactory(album=album, file=music_file)
        TrackFileFactory(track=track, file=music_file)
        TrackFileFactory(track=track, file=gtp_file)
        self.stdout.write(self.style.SUCCESS(f'{album.name} - {track.name}'))

    def handle(self, *args, **options):
        """Execute command."""
        # Music
        # ====================================================================

        albums = AlbumFactory.create_batch(4)

        self.music_category = FileCategoryFactory(name='Музыка')
        self.gtp_category = FileCategoryFactory(name='GTP')

        for album in albums:
            for i in range(5):
                self.create_track(album=album)

        # Blog
        # ====================================================================

        blogs = BlogEntryFactory.create_batch(12, create_images=True)
        self.stdout.write(self.style.SUCCESS('\nCreated blog entries'))

        series = BlogSeriesFactory.create_batch(3)
        for index, series_entry in enumerate(series):
            BlogSeriesItemFactory(
                series=series_entry,
                entry=blogs[index],
            )
            BlogSeriesItemFactory(
                series=series_entry,
                entry=blogs[index + 1],
            )
        self.stdout.write(self.style.SUCCESS('\nCreated blog series'))

        # Final
        # ====================================================================

        self.stdout.write(self.style.SUCCESS('DB successfully populated!'))
