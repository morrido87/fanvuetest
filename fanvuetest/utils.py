import csv
from io import StringIO

from albums.models import Album, AlbumBatchFile
from artists.models import Artist
from genres.models import Genre


def create_fake_data():
    """
    Creates fake artists, genres and albums data.
    """
    pop = Genre.objects.get_or_create(name="Pop")[0]
    rock = Genre.objects.get_or_create(name="Rock")[0]
    queen = Artist.objects.get_or_create(name="Queen", genre=rock)[0]
    gaga = Artist.objects.get_or_create(name="Lady Gaga", genre=pop)[0]
    nirvana = Artist.objects.get_or_create(name="Nirvana", genre=rock)[0]
    adele = Artist.objects.get_or_create(name="Adele", genre=pop)[0]
    Album.objects.create(name="A Night at the Opera", year=1975, artist=queen)
    Album.objects.create(name="Greatest Hits", year=1981, artist=queen)
    Album.objects.create(name="The Fame", year=2008, artist=gaga)
    Album.objects.create(name="Born This Way", year=2011, artist=gaga)
    Album.objects.create(name="Nevermind", year=1991, artist=nirvana)
    Album.objects.create(name="In Utero", year=1993, artist=nirvana)
    Album.objects.create(name="21", year=2011, artist=adele)
    Album.objects.create(name="25", year=2015, artist=adele)


def process_csv_file(file: AlbumBatchFile):
    file_data = file.file.read().decode('utf-8')
    csv_data = csv.reader(StringIO(file_data), delimiter=',')

    line_count = 0
    for line in csv_data:
        if line_count > 0:
            try:
                genre = Genre.objects.get_or_create(
                    name=line[4])[0]

                artist = Artist.objects.get_or_create(
                    name=line[3], genre=genre)[0]

                Album.objects.get_or_create(
                    name=line[2],
                    year=line[1],
                    artist=artist
                )
            except Exception as e:
                pass
        line_count += 1
