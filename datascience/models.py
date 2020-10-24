from django.db import models
from journal.models import Entry


class SentimentScore(models.Model):

    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    sentiment = models.FloatField()
    updated_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, entry: Entry):
        # ToDo use model to produce sentiment from text
        score = cls(entry=entry, sentiment=0.5)
        return score
