from django.db import models
from fontawesome.fields import IconField

class Category(models.Model):
    icon = IconField()

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title +' - '+ self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    song_duration = models.CharField(max_length=100)

    def __str__(self):
        return self.song_title +' - '+ self.file_type