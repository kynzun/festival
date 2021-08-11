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
    return render(request, "artist_view.html", {"artist": artist})
