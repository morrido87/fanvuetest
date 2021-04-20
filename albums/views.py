from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Album
from .serializers import AlbumsSerializer, AlbumBatchFileSerializer


class Pagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


class AlbumReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = []

    queryset = Album.objects.all()
    serializer_class = AlbumsSerializer
    pagination_class = Pagination


class AlbumsBatchUploadView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def put(self, request):
        serializer = AlbumBatchFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
