from django.urls import path

from .views import ArtistListView, ArtistDetailView

urlpatterns = [
    path('list', ArtistListView.as_view(), name='list_artists'),
    path('<int:pk>', ArtistDetailView.as_view(), name="view_artists"),
]
