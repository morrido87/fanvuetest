from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Album
from .serializers import AlbumsSerializer


class Pagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


class AlbumReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = []

    queryset = Album.objects.all()
    serializer_class = AlbumsSerializer
    pagination_class = Pagination
