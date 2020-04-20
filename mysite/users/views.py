from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from .forms import UserRegisterForm

def register_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserRegisterForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('/login')
        context = {
            'form': form
        }
        return render(request, "register.html", context)

def login_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or password is incorrect")

        context = {}

        return render(request, "login.html", context)

def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('login')