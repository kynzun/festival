from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser


# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)

        return redirect("home")
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("home")
    else:
        form = RegisterForm()
        return render(request, "signup.html", {"form": form})


@login_required
def mypage_view(request):
    user = request.user
    context = {
        "username": user.username,
        "email": user.email,
        "university": user.university,
        "like_artists": user.like_artists,
    }
    return render(request, "mypage.html", context=context)
