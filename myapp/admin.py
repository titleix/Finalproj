from django.contrib import admin
from .models import Profile, Todo, Forum, Comment

admin.site.register(Profile)
admin.site.register(Todo)
admin.site.register(Forum)
admin.site.register(Comment)


def __str__(self):
    return self.comment

# Register your models here.
