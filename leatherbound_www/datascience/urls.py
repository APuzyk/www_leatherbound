from django.urls import path
from . import views


urlpatterns = [
    path("api/datascience/sentiment", views.SentimentScoreList.as_view()),
]
