from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def notes_view(request):
    return HttpResponse("Hello from Notes app.")