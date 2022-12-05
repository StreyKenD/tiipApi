from fastapi import Request, FastAPI
# from sentimentAnalysis import get_sentiments
from database import doQuery

app = FastAPI()

@app.get('/getSentiment')
# async def getSentiment(request: Request):
async def getSentiment(post_id: int, body: str):
    # content = await request.json()
    result = 'None'
    if post_id is not None and body is not None:
        # result = get_sentiments(post_id, body)
        result = doQuery(post_id)

    return result

