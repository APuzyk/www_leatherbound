from django.db import models
from journal.models import Entry
import requests


class SentimentScore(models.Model):

    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    sentiment = models.FloatField()
    updated_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, entry: Entry):
        # ToDo use model to produce sentiment from text
        sentiment_score = cls.get_sentiment_score(entry.content)
        score = cls(entry=entry, sentiment=sentiment_score)
        return score

    @staticmethod
    def get_sentiment_score(content: str, url: str = "http://127.0.0.1:5000/") -> float:
        response = requests.get(url, {"query": content})
        return response.json()["sentiment"][0]
