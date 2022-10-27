from django.db import models
from datetime import datetime
# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    def __str__(self):
        return self.first_name
    
class Song(models.Model):
    title = models.CharField(max_length=30)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    
class Lyric(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=5000)
    songs_id = models.CharField(max_length=20)
    def __str__(self):
         return self.content