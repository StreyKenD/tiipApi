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

        # if (value >= 0.05):
        #     commentary.sentiment = 'positive'
        # elif (value > -0.05) and (value < 0.05):
        #     commentary.sentiment = 'neutral'
        # elif (value <= 0.05):
        #     commentary.sentiment = 'negative'
        sentiments.append(commentary)

    # so deixa as linhas onde o sentimento é compound
    sentiment = sentiments[sentiments.sentiment_type == 'compound']

    print(sentiment)


    return { "Mensagem": "ola" }




## usar isso?
# def remove_noise(tweet_tokens, stop_words = ()):
def remove_noise(sentece):

    # removido caracteres não alfabeticos
    sentece = sentece.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    #remove caracteres unicode
    sentece = sentece.replace(r'\r+|\n+|\t+','', regex=True)

    # covertido para lower-case
    sentece = sentece.str.casefold()

    # cleaned_tokens = []

    # for token, tag in pos_tag(tweet_tokens):
    #     token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
    #                    '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
    #     token = re.sub("(@[A-Za-z0-9_]+)","", token)

    #     if tag.startswith("NN"):
    #         pos = 'n'
    #     elif tag.startswith('VB'):
    #         pos = 'v'
    #     else:
    #         pos = 'a'

    #     lemmatizer = WordNetLemmatizer()
    #     token = lemmatizer.lemmatize(token, pos)

    #     if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
    #         cleaned_tokens.append(token.lower())
    return cleaned_tokens