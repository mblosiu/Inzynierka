from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

def homepage_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return render(request, "home.html", {})
    else:
        return render(request, "about.html", {})

def regulations_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "home.html", {})