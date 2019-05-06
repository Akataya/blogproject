from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
