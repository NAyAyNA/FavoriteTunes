from django.conf import settings
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=250)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
