
from django.urls import path
from . import views
from .views import (
    NoteListView, NoteCreateView, NoteDetailView,
    NoteUpdateView, NoteDeleteView
)



urlpatterns = [
    # path('', views.notes_view, name='notes'),
    # path('notes_list/', views.notes_list, name='notes_list'),
    # path('my_notes/', views.my_notes, name='my_notes'),
    # path('categories/', views.category_list, name='category_list'),
    # path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    #


path('notes/', NoteListView.as_view(), name='note_list'),
path('notes/add/', NoteCreateView.as_view(), name='note_add'),
path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
path('notes/<int:pk>/edit/', NoteUpdateView.as_view(), name='note_edit'),
path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
]
