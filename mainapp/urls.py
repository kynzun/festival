from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("artistView/<str:name>", artist_view, name="artistView"),
]
