# from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from journal.permissions import IsOwner
from .models import SentimentScore
from .serializers import SentimentScoreSerializer
from django.contrib.auth.models import User


class SentimentScoreList(generics.ListAPIView):
    queryset = SentimentScore.objects.all()
    serializer_class = SentimentScoreSerializer
    permission_classes = [IsOwner, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return SentimentScore.objects.filter(entry__author=user).order_by("-created_on")
