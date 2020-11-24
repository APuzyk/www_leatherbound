from django.db import models
from journal.models import Entry
from mr_modeling.predictor.predictor import Predictor
import pickle


predictor = pickle.load(open("/opt/models/predictor.p", "rb"))


class SentimentScore(models.Model):

    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    sentiment = models.FloatField()
    updated_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, entry: Entry):
        sentiment_score = cls.get_sentiment_score(entry.content)
        score = cls(entry=entry, sentiment=sentiment_score)
        return score

    @staticmethod
    def get_sentiment_score(content: str) -> float:
        sentiment_arr = predictor.get_prediction(content)
        return sentiment_arr[0]
