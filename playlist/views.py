from django.shortcuts import get_object_or_404, render 
from .models import Playlist
from song.models import Song
from django.http import JsonResponse, response, HttpResponse, HttpResponseForbidden

song = Song.objects.all()

def playlist_home(request):
    playlist = Playlist.objects.all()
    return render(request, 'playlist/playlist.html', {'playlist':playlist})

def playlist_songs(request, **kwargs):
    pl_id = kwargs['pk']
    current = Playlist.objects.filter(id=pl_id).first()
    songs = []
    owner = False
    if request.user.profile == current.author:
        owner = True
    all_songs = Song.objects.all()
    for song in all_songs:
        if song in current.parts.all():
            songs.append(song)
    return render(request, 'playlist/playlist_songs_list.html', {'songs':songs,'owner':owner,'pl_id': pl_id, 'playlist':current} )
    
def playlist_add_songs_list(request, **kwargs):
    pl_id = kwargs['pl']
    current = Playlist.objects.filter(id=pl_id).first()
    print(request.user.profile)
    print(current.author)
    if request.user.profile == current.author:
        songs = []
        all_songs = Song.objects.all()
        for song in all_songs:
            if song not in current.parts.all():
                songs.append(song)
        return render(request, 'playlist/songs_to_add_pl.html', {'songs':songs,'pl_id': pl_id, 'playlist':current} )
    else:
        return HttpResponse(f"<h1>Sorry {request.user}, you are not authorized to do this</h1>")
    
def add_remove_song(request):
    # if request.is_ajax():
        pk = request.POST.get('pk')
        obj = Song.objects.get(pk=pk)
        if obj.add_in_pl == True:
            obj.add_in_pl = False
            obj.save()
            add_in_pl = False
        else:
            obj.add_in_pl = True
            obj.save()
            add_in_pl = True
        return JsonResponse({'add_in_pl': add_in_pl})

def final_add_songs_pl(request):
    # if request.is_ajax():
        pl = request.POST.get('pl')
        obj = Playlist.objects.get(pk=pl)
        allSongs = Song.objects.all()
        for song in allSongs:
            if song.add_in_pl == True:
                obj.parts.add(song)
                song.add_in_pl = False
                obj.save()
                song.save()
        return JsonResponse({'pl':pl})

# def load_playlist_view(request):
#     data = Playlist.objects.all()
#     playlist = []
#     for obj in data:
    #     item = {
    #         'artist': obj.artist,
    #         'author': obj.author.user.username,
    #         'date_posted': obj.date_posted,
    #         'description': obj.description,
    #         'genre': obj.genre,
    #         'language': obj.language,
    #         'title': obj.title,
    #         'parts': obj.parts.all(),
    #     }

    #     playlist.append(item)
    # return JsonResponse({'playlist':playlist})
    
    