from django.urls import path
from . import views  # import your app's views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
]