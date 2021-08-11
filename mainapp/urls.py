from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("artistView/<str:name>", artist_view, name="artistView"),
    path("artistVote/<str:name>", artist_vote, name="artistVote"),
    path("categoryView/<str:category>", category_view, name="categoryView"),
]
