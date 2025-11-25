from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Notes(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    reminder = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notes",
        null=True,
        blank=True
    )

    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


# class NotesGroup(models.Model):
#     title = models.CharField(max_length=100)
#     notes = models.ManyToManyField(Notes)
#     members = models.ManyToManyField(User,related_name='notes_members')
#
#
#     def __str__(self):
#         return self.name




