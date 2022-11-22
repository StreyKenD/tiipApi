import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
# Function called in the api

def get_sentiments(commentary):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(commentary.sentence)
    sentiments = []
    for key, value in scores.items():
        commentary.sentiment_type = key
        commentary.sentiment_score = value

        sentiments.append(commentary)

    # so deixa as linhas onde o sentimento é compound
    sentiment = sentiments[sentiments.sentiment_type == 'compound']

    print(sentiment)


    return { "Mensagem": "ola" }
