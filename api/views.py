from django.views.generic import ListView

from genres.models import Genre


class GenresView(ListView):
    queryset = Genre.objects.all()
    context_object_name = "genres"



