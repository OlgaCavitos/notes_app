from django.shortcuts import render
from .models import Note, Category


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

def my_notes(request):
    notes = Note.objects.select_related('category').all()
    categories = Category.objects.all()
    return render(request, 'my_notes.html', {
        'notes': notes,
        'categories': categories
    })


def category_list(request):
    categories = Category.objects.prefetch_related('notes').all()
    return render(request, 'categories.html', {'categories': categories})


def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    notes = category.notes.all()
    return render(request, 'category_detail.html', {'category': category, 'notes': notes})