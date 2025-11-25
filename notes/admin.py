from django.contrib import admin

# Register your models here.

from .models import Notes,Category


class NotesAdmin(admin.ModelAdmin):

    list_display = ('title', 'text', 'reminder')
    search_fields = ['title', 'text', 'reminder']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','id')
    search_fields = ['title','id']


admin.site.register(Notes, NotesAdmin)
admin.site.register(Category, CategoryAdmin)