from rest_framework import serializers

from albums.serializers import AlbumsSerializer
from .models import Artist


class ArtistsSerializer(serializers.ModelSerializer):
    albums = AlbumsSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'albums')
