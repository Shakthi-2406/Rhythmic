"""Rythmic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from playlist import views as playlist_view
from profiles import views as profiles_view
from song import views as song_view
from users import views as users_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('song.urls', namespace='song')),
    path('playlist/', include('playlist.urls', namespace='playlist')),
    path('songs/<int:pk>/', playlist_view.playlist_songs , name="playlist-songs"),
    path('playlist/', playlist_view.playlist_home , name="playlist-home"),
    path('', song_view.home , name="song-home"),
    path('favorites/', song_view.favorites , name="favorites"),
    path('new/', song_view.new_song_form , name="new_song_form"),
    path('edit/<int:pk>/', song_view.edit_song_form , name="edit-song"),
    
    path('accounts/profile/', song_view.home , name="song-home"),
    path('register/', users_view.register , name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),


    path('profile/<int:upk>/', profiles_view.show_profile, name='show-profile'),
    path('favorites/<int:pk>/', song_view.fav_song_detail , name="fav_song_detail"),

    path('like_unlike_song/', song_view.like_unlike_song , name="like_unlike_song"),
    path('add_remove_song/', playlist_view.add_remove_song , name="add_remove_song"),
    path('final_add_songs_pl/', playlist_view.final_add_songs_pl , name="final_add_songs_pl"),
    path('songs/detail/<int:pk>/', song_view.song_detail , name="song-detail"),
    path('songs/detail/<int:pk>/<int:pl>/', song_view.playlist_song_detail , name="playlist-song-detail"),
    path('pl/songs/add/<int:pl>/', playlist_view.playlist_add_songs_list , name="songs-list-add-pl"),
]

urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
