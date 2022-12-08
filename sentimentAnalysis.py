import pandas as pd
import matplotlib.pyplot as plt
import nltk
from googletrans import Translator
from googletrans.constants import LANGUAGES
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def get_sentiments_all(text):
    sid = SentimentIntensityAnalyzer()

    # formattedBody = format(text)
    translatedBody = translate(text)
    scores = sid.polarity_scores(translatedBody)
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

    return sentimentFiltered


# def formattedBody(body):
    # removido caracteres não alfabeticos
    # body = body.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    #remove caracteres unicode
    # body = body.replace(r'\r+|\n+|\t+','', regex=True)

    # covertido para lower-case
    # body = body.str.casefold()

    #remove numeros
    # body = body.str.replace('\d+', '')

def translate(text):
    translator = Translator()
    translated = translator.translate(text, dest='en').text

    return translated