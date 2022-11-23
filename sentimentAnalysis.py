import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
# Function called in the api

def get_sentiments(payload):
    sid = SentimentIntensityAnalyzer()

    scores = sid.polarity_scores(payload['body'])
    sentiments = []

    for key, value in scores.items():
        commentary = {
            "sentiment_type": '',
            "sentiment_score": ''
        }
        commentary["sentiment_type"] = key
        commentary["sentiment_score"] = value
        sentiments.append(commentary)

    # so deixa as linhas onde o sentimento é compound
    filtered = next(x for x in sentiments if x['sentiment_type'] == 'compound')	

    return filtered
