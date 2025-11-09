from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def notes_view(request):
    return HttpResponse("Hello from Notes_app.")


def notes_list(request):
    notes = [
        {
            "title": "To do Homework",
            "content": ["Math", "Physics", "Geography"]
        },
        {
            "title": "Water the flowers",
            "content": ["Zamioculcas", "Violet", "Olive Tree"]
        },
        {
            "title": "Swimming",
            "content": ["Swim 5 km at 14:00"]
        },
    ]

    return render(request, "index.html", {'notes': notes, 'page_title': 'My notes'})
