from django.db import models
from datetime import datetime


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/images/')
    summary = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.summary
