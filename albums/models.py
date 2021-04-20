from django.db import models
from django.utils import timezone


class Album(models.Model):
    artist = models.ForeignKey(
        'artists.Artist',
        related_name="albums",
        null=False,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=50
    )

    year = models.SmallIntegerField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    updated_at = models.DateTimeField(
        editable=False
    )

    class Meta:
        ordering = ('name',)
        unique_together = ('artist', 'name')

    def save(self, *args, **kwargs):
        self.updated_at = timezone.localtime()
        super(Album, self).save(*args, **kwargs)
