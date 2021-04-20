from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Genre
from .serializers import GenresSerializer


class Pagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


class GenresReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = []

    queryset = Genre.objects.all()
    serializer_class = GenresSerializer
    pagination_class = Pagination


def genres_view(request):
    genres = Genre.objects.all()
    serializer = GenresSerializer(genres, many=True)
    genres_counters = Genre.objects.artists_count()
    context = {
        "genres": serializer.data,
        "count": genres_counters
    }
    return render(request, template_name='genres.html', context=context)


def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    context = {
        "genre": genre
    }
    return render(request, template_name='genre.html', context=context)
