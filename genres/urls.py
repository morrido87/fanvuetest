from django.urls import path

from .views import GenreListView, GenreDetailView

urlpatterns = [
    path('list', GenreListView.as_view(), name='list_genres'),
    path('<int:pk>', GenreDetailView.as_view(), name="view_genre"),
]
