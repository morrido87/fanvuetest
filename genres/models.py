from django.db import models
from django.db.models import Count, Q
from django.utils import timezone

from artists.models import Artist


class GenreManager(models.Manager):
    def artists_count(self, subquery=~Q(pk=None)):
        return self.values('name').\
            annotate(total=Count('artists__id', filter=subquery)).\
            order_by('id')


class Genre(models.Model):
    name = models.CharField(
        max_length=50
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    updated_at = models.DateTimeField(
        editable=False
    )

    objects = GenreManager()

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.localtime()
        super(Genre, self).save(*args, **kwargs)
