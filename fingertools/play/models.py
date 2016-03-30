from django.db import models
from fingertools.base.models import FTObject

# Create your models here.

class Playlist(FTObject):
    public = models.BooleanField()
    name = models.TextField()

class Music(models.Model):
    artist = models.TextField(null=True)
    name = models.TextField(null=True)
    album = models.TextField(null=True)
    year = models.PositiveSmallIntegerField(null=True)
    length = models.FloatField(null=True)
    filename = models.TextField()
    url = models.TextField()
    rating = models.PositiveSmallIntegerField()
    views = models.PositiveIntegerField()
    playlist = models.ForeignKey(Playlist, null=False)
    