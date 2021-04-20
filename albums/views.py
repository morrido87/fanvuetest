from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Album
from .serializers import AlbumsSerializer


class Pagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


class AlbumDetailView(RetrieveAPIView):
    permission_classes = []

    queryset = Album.objects.all()
    serializer_class = AlbumsSerializer


class AlbumListView(ListAPIView):
    permission_classes = []
    pagination_class = Pagination

    queryset = Album.objects.all()
    serializer_class = AlbumsSerializer
