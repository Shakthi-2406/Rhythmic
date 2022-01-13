from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from profiles.models import Profile


GENRE_CHOICES = (
    ("Unknown", "Unknown"),
    ("Romantic", "Romantic"),
    ("Motivational", "Motivational"),
    ("Heart broken", "Heart broken"),
    ("Rock", "Rock")
)

LANG_CHOICES = (
    ("Unknown", "Unknown"),
    ("Tamil", "Tamil"),
    ("English", "English"),
    ("Hindi", "Hindi"),
    ("Malayalam", "Malayalam"),
    ("Telugu", "Telugu"),
    ("Kanada", "Kanada")
)


class Song(models.Model):
    title = models.CharField(max_length=100, null=False)
    movie_name = models.CharField(max_length=100, null=True, blank=True, default="Unknown")
    artist = models.CharField(max_length=100, null=True, blank=True, default="Unknown")
    genre = models.CharField(max_length=15, choices= GENRE_CHOICES, default= "Unknown")
    language = models.CharField(max_length=10, choices= LANG_CHOICES, default= "Unknown")
    lyrics = models.TextField(default="Currently Unavailable",null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Profile,on_delete= models.SET_NULL,null=True)
    liked = models.ManyToManyField(User, blank=True)
    file = models.FileField(default='default.mp3',upload_to='musics/',null=True,blank=True)
    duration = models.PositiveIntegerField("Duration in seconds",blank=True,null=True)
    cover = models.ImageField(default='default.jpeg', upload_to='covers/',null=True,blank=True)
    add_in_pl = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    @property
    def liked_count(self):
        return self.liked.all().count()

    class Meta:
        ordering = ("-date_posted",)
