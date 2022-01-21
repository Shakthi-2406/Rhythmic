from django.contrib import auth
from django.http.response import HttpResponseRedirect
from profiles.models import Profile
from .models import Song
from django.shortcuts import render
from django.http import JsonResponse
from playlist.models import Playlist
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import mutagen
from .forms import SongForm



def new_song_form(request):
    if request.method == 'POST':
        form = SongForm(request.POST,request.FILES)

        if form.is_valid():
            author = Profile.objects.get(user = request.user)
            instance = form.save(commit=False)
            instance.author = author
            instance.save()
            # RETURNING TO HOME PAGE
            return HttpResponseRedirect('/')
    else:
        form = SongForm()

    return render(request, 'song/newsong.html', {'form':form})

def edit_song_form(request,*args, **kwargs):
    song_id = kwargs['pk']
    song = Song.objects.filter(id=song_id).first()
    if request.method == 'POST':
        form = SongForm(request.POST,request.FILES, instance=song)

        if form.is_valid():
            song = form.save(commit=False)
            song.save()
            # RETURNING TO HOME PAGE
            return HttpResponseRedirect('/')
    else:
        form = SongForm(instance=song)

    return render(request, 'song/newsong.html', {'form':form})


@receiver(pre_save, sender=Song)
def song_save_calculate_duration(sender, instance, raw, using, update_fields, **kwargs):
    print(sender)
    print(update_fields)
    file_was_updated = False
    if hasattr(instance.file, 'file'):
        file_was_updated = True
    if update_fields and 'file' in update_fields:
        file_was_updated = True
    if file_was_updated:
        audio_info = mutagen.File(instance.file).info
        instance.duration = int(audio_info.length)
        print("Success!!!")
    else:
        print("file not changed")



def home(request):
    # ANY CHANGE HERE, CHANGE LINE 23 TOO PLS
    songs = Song.objects.all()
    return render(request, 'song/home.html', {'songs':songs} )


def favorites(request):
    items = Song.objects.all()
    favsongs =[]
    fav = True
    for item in items:
        if request.user in item.liked.all():
            favsongs.append(item)
    return render(request, 'song/home.html', {'songs':favsongs, 'tit':'FAVOURITES', 'fav':fav} )


def fav_song_detail(request,**kwargs):
    song_id = kwargs['pk']
    array=[]
    items = Song.objects.all()
    favsongs =[]
    fav = True
    for item in items:
        if request.user in item.liked.all():
            favsongs.append(item)
    available_data = favsongs

    for data in available_data:
        array.append(data.id)
    upper = len(array)
    current_index = array.index(song_id)
    if current_index == 0:
        previous = array[upper-1]
    else:
        previous = array[current_index-1]
    if current_index == upper-1:
        next = array[0]
    else:
        next = array[current_index+1]
    current = Song.objects.filter(id=song_id).first()
    if request.user in current.liked.all():
        liked = True
    else:
        liked = False
    return render(request, 'song/song-detail.html', {'song': current,'fav':fav,'liked':liked,'id': song_id,'next_id':next,'previous_id':previous} )


def song_detail(request,**kwargs):
    song_id = kwargs['pk']
    array=[]
    available_data = Song.objects.all()

    for data in available_data:
        array.append(data.id)
    upper = len(array)
    current_index = array.index(song_id)
    if current_index == 0:
        previous = array[upper-1]
    else:
        previous = array[current_index-1]
    if current_index == upper-1:
        next = array[0]
    else:
        next = array[current_index+1]
    current = Song.objects.filter(id=song_id).first()
    if request.user in current.liked.all():
        liked = True
    else:
        liked = False
    return render(request, 'song/song-detail.html', {'song': current,'liked':liked,'id': song_id,'next_id':next,'previous_id':previous} )





def playlist_song_detail(request,**kwargs):
    play = True
    song_id = kwargs['pk']
    pl_id = kwargs['pl']
    current_pl = Playlist.objects.filter(id=pl_id).first()
    songs_in_pl = []
    all_songs = Song.objects.all()

    for song in all_songs:
        if song in current_pl.parts.all():
            songs_in_pl.append(song)

    array=[]
    available_data = songs_in_pl

    for data in available_data:
        array.append(data.id)

    upper = len(array)
    current_index = array.index(song_id)
    if upper == 1:
        previous = array[current_index]
        next = array[current_index]
    else:
        if current_index == 0:
            previous = array[upper-1]
        else:
            previous = array[current_index-1]
        if current_index == upper-1:
            next = array[0]
        else:
            next = array[current_index+1]
    current = Song.objects.filter(id=song_id).first()
    if request.user in current.liked.all():
        liked = True
    else:
        liked = False
    return render(request, 'song/song-detail.html', {'song': current,'play':play,'liked':liked,'playlist':current_pl,'id': song_id,'next_id':next,'previous_id':previous,'pl':pl_id} )


def like_unlike_song(request):
    # if request.is_ajax():
        pk = request.POST.get('pk')
        obj = Song.objects.get(pk=pk)
        if request.user in obj.liked.all():
            liked = False
            obj.liked.remove(request.user)
        else:
            liked = True
            obj.liked.add(request.user)
        return JsonResponse({'liked':liked, 'liked_count':obj.liked_count})



# def load_song_view(request):
#     data = Song.objects.all()
#     songs = []
#     for obj in data:
#         item = {
#             'artist': obj.artist,
#             'author': obj.author.user.username,
#             'date_posted': obj.date_posted,
#             'genre': obj.genre,
#             'language': obj.language,
#             'liked': obj.liked,
#             'lyrics': obj.lyrics,
#             'movie_name': obj.movie_name,
#             'title': obj.title
#         }
#         songs.append(item)
#     return JsonResponse({'songs':songs})
    
    