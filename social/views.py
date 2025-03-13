from django.shortcuts import render, redirect
from .models import Profile


def profile(request, username):
    profile = Profile.objects.get(username=username)
    context = {'profile': profile}
    return render(request, 'social/profile.html', context)
