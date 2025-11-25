from django.shortcuts import render, redirect


from .forms import NoteForm, LoginForm, RegisterForm
from .models import Notes, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class NoteListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Notes
    template_name = "note_list.html"
    context_object_name = "notes"

    def get_queryset(self):
        queryset = Notes.objects.filter(owner=self.request.user)

        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category__id=category_id)

        if self.request.GET.get('group') == '1':
            # Get notes owned by the user
            user_notes = Notes.objects.filter(owner=self.request.user)

            # Get notes belonging to any of the user's groups
            group_notes = Notes.objects.filter(group__in=self.request.user.groups.all())

            # Combine them with union
            queryset = (user_notes | group_notes).distinct()

            # If category filter was applied, re-apply it
            if category_id:
                queryset = queryset.filter(category__id=category_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['show_group'] = self.request.GET.get('group') == '1'
        return context

class NoteCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Notes
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("note_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class NoteDetailView(DetailView):
    model = Notes
    template_name = "note_detail.html"



class NoteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Notes
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("note_list")

    def get_queryset(self):
        return Notes.objects.filter(owner=self.request.user)

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Notes
    template_name = "note_delete.html"
    success_url = reverse_lazy("note_list")

    def get_queryset(self):
        return Notes.objects.filter(owner=self.request.user)





def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in{username}.")
                return redirect('note_list')
            else:
                messages.error(request, f"Invalid username or password.")
        return render(request, "login.html", {"form": form})


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "register.html", {"form": form})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"You are now registered{user.username}.")
            return redirect ('note_list')
        return render(request, 'register.html', {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "You are now logged out.")
    return redirect('login')