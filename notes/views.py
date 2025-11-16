from django.shortcuts import render

from .forms import NoteForm
from .models import Notes, Category


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
    notes = Notes.objects.select_related('category').all()
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





from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Notes, Category
from .forms import NoteForm


class NoteListView(ListView):
    model = Notes
    template_name = "note_list.html"
    context_object_name = "notes"

    def get_queryset(self):
        queryset = Notes.objects.all()

        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category__id=category_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class NoteDetailView(DetailView):
    model = Notes
    template_name = "note_detail.html"


class NoteCreateView(CreateView):
    model = Notes
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("note_list")


class NoteUpdateView(UpdateView):
    model = Notes
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("note_list")


class NoteDeleteView(DeleteView):
    model = Notes
    template_name = "note_delete.html"
    success_url = reverse_lazy("note_list")

