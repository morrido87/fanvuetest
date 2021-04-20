from django.core.management.base import BaseCommand

from fanvuetest.utils import create_fake_data


class Command(BaseCommand):
    """Management command to create fake data for artists, genres and albums.
    """

    help = """Creates fake data for artists, genres and albums."""

    def handle(self, *args, **options):
        create_fake_data()
        exit(0)
