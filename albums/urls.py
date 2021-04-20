from django.urls import path

from .views import AlbumListView, AlbumDetailView

urlpatterns = [
    path('list', AlbumListView.as_view(), name='list_albums'),
    path('<int:pk>', AlbumDetailView.as_view(), name="view_album"),
]
