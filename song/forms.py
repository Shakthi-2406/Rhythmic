from django import forms
from django.contrib.auth import models
from django.forms import fields
from .models import Song, GENRE_CHOICES,LANG_CHOICES




    # title = models.CharField(max_length=100, null=False)
    # movie_name = models.CharField(max_length=100, null=True, blank=True, default="Unknown")
    # artist = models.CharField(max_length=100, null=True, blank=True, default="Unknown")
    # genre = models.CharField(max_length=15, choices= GENRE_CHOICES, default= "Unknown")
    # language = models.CharField(max_length=10, choices= LANG_CHOICES, default= "Unknown")
    # lyrics = models.TextField(default="Currently Unavailable",null=True,blank=True)
    # date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(Profile,on_delete= models.SET_NULL,null=True)
    # liked = models.ManyToManyField(User, blank=True)
    # file = models.FileField(default='default.mp3',upload_to='musics/')
    # duration = models.PositiveIntegerField("Duration in seconds",blank=True,null=True)
    # cover = models.ImageField(default='default.jpeg', upload_to='covers/')

class SongForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True)
    movie_name = forms.CharField(max_length=100, required=False)
    artist = forms.CharField(max_length=100, required=False)
    genre = forms.ChoiceField(choices= GENRE_CHOICES, required=False)
    language = forms.ChoiceField(choices= LANG_CHOICES, required=True)
    file = forms.FileField(required=True)
    cover = forms.ImageField(required=False)

    class Meta:
        model = Song
        fields = ('title','movie_name','artist','genre','language','file','cover',)




