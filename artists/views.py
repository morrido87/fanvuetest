from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Artist
from .serializers import ArtistsSerializer


class Pagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


class ArtistDetailView(RetrieveAPIView):
    permission_classes = []

    queryset = Artist.objects.all()
    serializer_class = ArtistsSerializer


class ArtistListView(ListAPIView):
    permission_classes = []
    pagination_class = Pagination

    queryset = Artist.objects.all()
    serializer_class = ArtistsSerializer
