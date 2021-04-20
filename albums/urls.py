from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import AlbumsBatchUploadView

router = DefaultRouter()
router.register(r'api', views.AlbumReadOnlyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload', AlbumsBatchUploadView.as_view(), name="album_batch_upload")
]