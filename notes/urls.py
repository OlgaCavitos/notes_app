
from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_view, name='notes'),
    path('notes_list/', views.notes_list, name='notes_list'),

]