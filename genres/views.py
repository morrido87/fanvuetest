from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Genre
from .serializers import GenresSerializer


class Pagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


class GenreDetailView(RetrieveAPIView):
    permission_classes = []

    queryset = Genre.objects.all()
    serializer_class = GenresSerializer


class GenreListView(ListAPIView):
    permission_classes = []
    pagination_class = Pagination

    queryset = Genre.objects.all()
    serializer_class = GenresSerializer
