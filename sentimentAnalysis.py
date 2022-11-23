import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
# Function called in the api

def get_sentiments(payload):
    sid = SentimentIntensityAnalyzer()

    formattedBody = format(payload['body'])

    scores = sid.polarity_scores(formattedBody)
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


def formattedBody(body):
    # removido caracteres não alfabeticos
    body = body.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    #remove caracteres unicode
    body = body.replace(r'\r+|\n+|\t+','', regex=True)

    # covertido para lower-case
    body = body.str.casefold()

    #remove numeros
    body = body.str.replace('\d+', '')
