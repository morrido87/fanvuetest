from django.core.management.base import BaseCommand

from albums.models import AlbumBatchFile
from fanvuetest.utils import create_fake_data, process_csv_file


class Command(BaseCommand):
    """Management command to create fake data for artists, genres and albums.
    """

    help = """Creates fake data for artists, genres and albums."""

    def handle(self, *args, **options):
        files = AlbumBatchFile.objects.filter(processed=False)
        if files.exists():
            for file in files:
                process_csv_file(file)
        exit(0)
