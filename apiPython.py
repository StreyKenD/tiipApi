from fastapi import Request, FastAPI
from sentimentAnalysis import get_sentiments

app = FastAPI()

@app.get('/getSentiment')
async def getSentiment(request: Request):
    content = await request.json()
    result = 'None'
    if content is not None:
        result = get_sentiments(content)

    return result

