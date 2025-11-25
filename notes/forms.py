from django import forms
from .models import Notes, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text', 'reminder', 'category']
        widgets = {
            'reminder': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
