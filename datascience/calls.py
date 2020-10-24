from .models import SentimentScore


def runEntryModels(entry):
    runSentimentScore(entry)


def runSentimentScore(entry):
    print(entry.content)
    score = SentimentScore.create(entry)
    score.save()
