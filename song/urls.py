from django.urls import path
from .views import (
    home,
    # load_song_view,
)

app_name = 'song'

urlpatterns = [
    path('', home, name='song-home'),
    # path('test/', load_song_view, name='test'),
]

