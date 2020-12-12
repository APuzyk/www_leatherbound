from . import models as m
from rest_framework import serializers


class SentimentScoreSerializer(serializers.ModelSerializer):
    entry_created_on = serializers.DateTimeField(source="entry.created_on")

    class Meta:
        model = m.SentimentScore
        fields = ["entry_created_on", "sentiment"]
