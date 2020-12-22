from django.db import models
from journal.models import Entry
import re
import numpy as np
import pickle
import onnxruntime as ort

sentiment_helper = pickle.load(open("/opt/models/sentiment_helper.p", "rb"))
ort_session = ort.InferenceSession("/opt/models/sentiment.onnx")


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
        text_vec = get_text_vec(
            content,
            sentiment_helper["word_dict"],
            sentiment_helper["text_input_size"]
        )
        sentiment_arr = ort_session.run(None, {"0": text_vec})

        return float(sentiment_arr[0][0][0])


def get_text_vec(text, word_dict, text_input_size):
    text = re.sub(r'<.*?>', '', text) #html tags
    text = re.sub(r'[^\w\s]', '', text) # punctuation
    text = text.lower()
    text = text.strip()    

    indexes = [word_dict.get(word, 0) for word in text]

    if len(indexes) > text_input_size:
        start = len(indexes) - text_input_size
        indexes = indexes[start:]
    else:
        [indexes.append(0) for _ in range(text_input_size - len(indexes))]
     
    return np.array([indexes])