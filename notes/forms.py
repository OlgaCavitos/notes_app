from django import forms
from .models import Notes, Category

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
