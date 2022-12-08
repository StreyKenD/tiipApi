from fastapi import Request, FastAPI
from database import doQuery

app = FastAPI()

@app.get('/getSentiment')
async def getSentiment(post_id: int, body: str):
    result = 'None'
    if post_id is not None and body is not None:
        result = doQuery(post_id)

    return result

