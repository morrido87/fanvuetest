from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Artist
from .serializers import ArtistsSerializer


class Pagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


class ArtistsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = []

    queryset = Artist.objects.all()
    serializer_class = ArtistsSerializer
    pagination_class = Pagination


def artists_view(request):
    artists = Artist.objects.all()
    serializer = ArtistsSerializer(artists, many=True)
    context = {
        "artists": serializer.data
    }
    return render(request, template_name='artists.html', context=context)


def artist_detail_view(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    context = {
        "artist": artist
    }
    return render(request, template_name='artist.html', context=context)
