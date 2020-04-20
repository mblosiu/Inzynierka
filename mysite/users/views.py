from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Customer
from .forms import CreateUserForm

def register_view(request, *args, **kwargs):
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        print(user)
        username = form.cleaned_data.get('username')

        Customer.objects.create(
            user=user,
            name=user.username,
        )
        messages.success(request, 'Account was created for ' + username)
        return redirect('/login')
    context = {'form': form}
    return render(request, "account/register.html", context)

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

        return render(request, "account/login.html", context)

def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def userView(request, *args, **kwargs):
    return render(request, "account/user.html")

@login_required(login_url='login')
def userProfileView(request, *args, **kwargs):
    name = request.user.customer.name
    surname = request.user.customer.surname
    email = request.user.customer.email
    birth_date = request.user.customer.birth_date

    context = {'name:': name,
               'surname:': surname,
               'email:': email,
               'birth_date:': birth_date,
               }
    return render(request, "account/userProfile.html", context)

@login_required(login_url='login')
def userSettingsView(request, *args, **kwargs):
    password = request.user.password
    name = request.user.customer.name
    surname = request.user.customer.surname
    email = request.user.customer.email
    birth_date = request.user.customer.birth_date

    context = {'name:': name,
               'surname:': surname,
               'email:': email,
               'birth_date:': birth_date,
               }
    return render(request, "account/settings.html", context)

@login_required(login_url='login')
def userProfileEditView(request, *args, **kwargs):
    password = request.user.password
    name = request.user.customer.name
    surname = request.user.customer.surname
    email = request.user.customer.email
    birth_date = request.user.customer.birth_date

    context = {'name:': name,
               'surname:': surname,
               'email:': email,
               'birth_date:': birth_date,
               }
    return render(request, "account/profileEdit.html", context)