from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(*args, **kwargs):
    return HttpResponse("Homepage")