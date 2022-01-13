from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import timezone
from profiles.models import Profile
from song.models import GENRE_CHOICES, LANG_CHOICES, Song

class Playlist(models.Model):
    title = models.CharField(max_length=100, null=False)
    movie_name = models.CharField(max_length=100, null=True, blank=True, default="Unknown")
    artist = models.CharField(max_length=100, null=True, blank=True, default="Unknown")
    genre = models.CharField(max_length=15,null=True, choices= GENRE_CHOICES, default= "Unknown")
    language = models.CharField(max_length=10,null=True, choices= LANG_CHOICES, default= "Unknown")
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile,on_delete= CASCADE,null=True)

    parts = models.ManyToManyField(Song, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    album_cover = models.ImageField(default='playDefault.jpeg', upload_to='album_covers/')



    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ("-date_posted",)
