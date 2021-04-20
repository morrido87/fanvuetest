import os
import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('batch', filename)


def extension_validator(filename):
    ext = filename.name.split('.')[-1].lower()
    valid_extensions = ['txt', 'csv']
    if ext not in valid_extensions:
        raise ValidationError(f"""
        Invalid extension. Extensions allowed are: {", ".join(valid_extensions)}
        """)


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


class AlbumBatchFile(models.Model):

    file = models.FileField(
        upload_to=upload_to,
        validators=[extension_validator],
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    processed = models.BooleanField(
        default=False
    )

    def save(self, *args, **kwargs):
        self.uploaded_at = timezone.localtime()
        super(AlbumBatchFile, self).save(*args, **kwargs)
