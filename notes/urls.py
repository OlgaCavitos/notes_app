
from django.urls import path
from . import views
from .views import (
    NoteListView, NoteCreateView, NoteDetailView,
    NoteUpdateView, NoteDeleteView,login_view, register_view, logout_view
)

from .views_auth import CustomLoginView, CustomLogoutView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('', views.notes_view, name='notes'),
    # path('notes_list/', views.notes_list, name='notes_list'),
    # path('my_notes/', views.my_notes, name='my_notes'),
    # path('categories/', views.category_list, name='category_list'),
    # path('categories/<int:category_id>/', views.category_detail, name='category_detail'),


path('notes/', NoteListView.as_view(), name='note_list'),
path('notes/add/', NoteCreateView.as_view(), name='note_add'),
path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
path('notes/<int:pk>/edit/', NoteUpdateView.as_view(), name='note_edit'),
path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
path('login/', login_view, name='login'),
path('register/', register_view, name='register'),
path('logout/', logout_view, name='logout'),
# path('login/', CustomLoginView.as_view(), name='login'),
# path('logout/', CustomLogoutView.as_view(), name='logout'),
# path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]

