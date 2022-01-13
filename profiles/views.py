from django.shortcuts import get_object_or_404, render 
from .models import Profile
from song.models import Song
from django.http import JsonResponse, response


def show_profile(request,**kwargs):
    upk = kwargs['upk']
    prof = Profile.objects.get(pk=upk)
    print(prof.user.username)
    return render(request, 'profiles/profile.html', {'prof':prof})

