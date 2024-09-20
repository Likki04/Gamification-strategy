# Bikeapp/models.py

from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Reward(models.Model):
    name = models.CharField(max_length=100)
    points_required = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    badges = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.user.username

    

