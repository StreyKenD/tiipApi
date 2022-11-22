from fastapi import FastAPI
from sentimentAnalysis import get_sentiments

app = FastAPI()

@app.get('/')
def getSentiment():

    result = get_sentiments()

    return result

