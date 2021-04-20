from rest_framework import serializers

from artists.serializers import ArtistsSerializer
from .models import Genre


class GenresSerializer(serializers.ModelSerializer):
    artists = ArtistsSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ('id', 'name', 'artists')
