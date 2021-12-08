from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # age = models.IntegerField(blank=True, null=True)
    # bio = models.TextField(blank=True, null=True)
    # image = models.ImageField(null=True, blank=True, upload_to='static/images/')


def __str__(self):
    return str(self.user)


class Forum(models.Model):
    name = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
    topic = models.CharField(max_length=300)
    description = models.TextField(max_length=1000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.topic


class Comment(models.Model):
    name = models.CharField(max_length=100, default=1)
    forum = models.ForeignKey(Forum, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)



