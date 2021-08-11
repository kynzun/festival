from django.shortcuts import get_object_or_404, redirect, render
from .models import Artist

# Create your views here.


def home(request):
    artists = Artist.objects.all()[:5]
    bidols = Artist.objects.filter(category="남자 아이돌")[:5]
    gidols = Artist.objects.filter(category="여자 아이돌")[:5]
    hiphops = Artist.objects.filter(category="힙합")[:5]
    indies = Artist.objects.filter(category="인디음악")[:5]
    ballads = Artist.objects.filter(category="발라드")[:5]
    bands = Artist.objects.filter(category="락밴드")[:5]
    return render(
        request,
        "home.html",
        {
            "artists": artists,
            "bidols": bidols,
            "gidols": gidols,
            "hiphops": hiphops,
            "indies": indies,
            "ballads": ballads,
            "bands": bands,
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
