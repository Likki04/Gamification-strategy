# Bikeapp/urls.py

from django.urls import path
from .views import ChallengeListView, RewardListView, UserProgressView

# Bikeapp/urls.py
from . import views

urlpatterns = [
    path('challenges/', views.challenges_view, name='challenges-view'),
    path('rewards/', views.rewards_view, name='rewards-view'),
    path('progress/', views.user_progress_view, name='user-progress-view'),
    path('api/challenges/', ChallengeListView.as_view(), name='challenges-list'),
    path('api/rewards/', RewardListView.as_view(), name='rewards-list'),
    path('api/progress/<str:username>/', UserProgressView.as_view(), name='user-progress'),
]
