from django.db import models
from django.utils import timezone


class URL(models.Model):
    original_url = models.URLField(max_length=512)
    visits = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.original_url - self.short_url
