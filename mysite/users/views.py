from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import UserRegisterForm

# Create your views here.

def register_view(request, *args, **kwargs):
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, "register.html", context)
