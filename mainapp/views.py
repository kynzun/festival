from django.shortcuts import get_object_or_404, redirect, render
from .models import Artist

# Create your views here.


def home(request):
    artists = Artist.objects.all()
    return render(
        request,
        "home.html",
        {
            "artists": artists,
        },
    )


def artist_view(request, name):
    artist = Artist.objects.get(name=name)
    user = request.user
    voted = False
    if artist in user.like_artists.all():
        voted = True
    return render(request, "artist_view.html", {"artist": artist, "voted": voted})


def artist_vote(request, name):
    artist = Artist.objects.get(name=name)
    user = request.user
    artist.like_users.add(user)
    return redirect("artistView", artist.name)


def category_view(request, category):
    artists = Artist.objects.filter(category=category)
    return render(request, "category_view.html", {"artists": artists})
