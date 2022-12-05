import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

from database import doQuery
# Function called in the api

def get_sentiments(post_id, body):
    sid = SentimentIntensityAnalyzer()

    formattedBody = format(body)

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
    sentimentFiltered = next(x for x in sentiments if x['sentiment_type'] == 'compound')	

    result = doQuery(post_id, body, sentimentFiltered)

    return result

# def get_sentiments_all(payload):
#     sid = SentimentIntensityAnalyzer()

#     formattedBody = format(payload[1])
#     scores = sid.polarity_scores(formattedBody)
#     sentiments = []

#     for key, value in scores.items():
#         commentary = {
#             "sentiment_type": '',
#             "sentiment_score": ''
#         }
#         commentary["sentiment_type"] = key
#         commentary["sentiment_score"] = value
#         sentiments.append(commentary)

#     # so deixa as linhas onde o sentimento é compound
#     sentimentFiltered = next(x for x in sentiments if x['sentiment_type'] == 'compound')	

#     return sentimentFiltered


def formattedBody(body):
    # removido caracteres não alfabeticos
    body = body.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    #remove caracteres unicode
    body = body.replace(r'\r+|\n+|\t+','', regex=True)

    # covertido para lower-case
    body = body.str.casefold()

    #remove numeros
    body = body.str.replace('\d+', '')
