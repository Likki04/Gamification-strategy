# Bikeapp/views.py
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Challenge, Reward, UserProgress
from .serializers import ChallengeSerializer, RewardSerializer, UserProgressSerializer
from rest_framework import status
class ChallengeListView(generics.ListCreateAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer


class RewardListView(generics.ListCreateAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer


class UserProgressView(generics.RetrieveUpdateAPIView):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer
    lookup_field = 'user__username'  # Keep this as it references the related field
    def get(self, request, username, *args, **kwargs):
        try:
            # Fetch UserProgress using the related user field (username)
            user_progress = UserProgress.objects.get(user__username=username)
            serializer = UserProgressSerializer(user_progress)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserProgress.DoesNotExist:
            return Response({"error": "User progress not found"}, status=status.HTTP_404_NOT_FOUND)


# Create your views here.
# Bikeapp/views.py


def challenges_view(request):
    return render(request, 'challenges.html')

def rewards_view(request):
    return render(request, 'rewards.html')

def user_progress_view(request):
    return render(request, 'progress.html')

def homepage_view(request):
    return render(request, 'Bikeapp/base.html')

