from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import genres_view, genre_detail_view, GenresReadOnlyViewSet

router = DefaultRouter()
router.register(r'api', GenresReadOnlyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('view', genres_view, name="list_genres"),
    path('view/<int:pk>', genre_detail_view, name="view_genre")
]
