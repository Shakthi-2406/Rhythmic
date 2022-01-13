from django.urls import path
from .views import (
    playlist_home,
    # load_playlist_view,
    playlist_songs,
)

app_name = 'playlist'

urlpatterns = [
    path('', playlist_home, name='playlist-home'),
    path('songs/', playlist_songs, name='playlist-songs'),
    # path('ajax/', load_playlist_view, name='playlist-ajax'),
]
