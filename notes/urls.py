
from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_view, name='notes'),
    path('notes_list/', views.notes_list, name='notes_list'),
    path('my_notes/', views.my_notes, name='my_notes'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
]