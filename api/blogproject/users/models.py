from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joined = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_author = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.PositiveIntegerField()
