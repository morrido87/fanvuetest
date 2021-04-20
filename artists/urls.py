from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import artists_view, artist_detail_view, ArtistsReadOnlyViewSet

router = DefaultRouter()
router.register(r'api', ArtistsReadOnlyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('view', artists_view, name="list_artists"),
    path('view/<int:pk>', artist_detail_view, name="view_artist")
]
