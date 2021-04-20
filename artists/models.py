from django.db import models
from django.utils import timezone


class Artist(models.Model):
    genre = models.ForeignKey(
        'genres.Genre',
        related_name="artists",
        null=False,
        on_delete=models.CASCADE
    )

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

    def save(self, *args, **kwargs):
        self.updated_at = timezone.localtime()
        super(Artist, self).save(*args, **kwargs)
