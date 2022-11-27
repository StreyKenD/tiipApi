import psycopg2
from config import config

def doQuery(payload, sentimentFiltered):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        query = "select * from comments where post_id = %s;"
        cur.execute(query, (payload['post_id'],))
        comments = cur.fetchall()  
        total_score=sentimentFiltered['sentiment_score']
        size=0

        for comment in comments:
            total_score += comment[2] if comment[2] != None else 0
            size += 1

        postScore = total_score / size
       
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            result = {
                "post_score": postScore,
                "comment_score": sentimentFiltered['sentiment_score']
            }
        return result
