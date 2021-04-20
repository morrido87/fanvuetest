from rest_framework import serializers

from .models import Album, AlbumBatchFile


class AlbumsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'name', 'year')


class AlbumBatchFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlbumBatchFile
        fields = '__all__'
