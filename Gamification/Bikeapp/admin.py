# Bikeapp/admin.py

from django.contrib import admin
from .models import Challenge, Reward, UserProgress

admin.site.register(Challenge)
admin.site.register(Reward)
admin.site.register(UserProgress)

# Register your models here.
