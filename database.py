import psycopg2
from config import config
from sentimentAnalysis import get_sentiments_all
import requests

def doQuery(post_id):
    """ Connect to the PostgreSQL database server """
    conn = None
    postScore = 0
    post = []
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        selectPost = "select * from posts where id = %s;"
        cur.execute(selectPost, (post_id,))
        post = cur.fetchall()

        if len(post) > 0:
            oldPostScore = post[0][2] 

            query = "select * from comments where post_id = %s;"
            cur.execute(query, (post_id,))
            comments = cur.fetchall()  
            total_score=0
            size=0

            for comment in comments:
                score = get_sentiments_all(comment[1])
                print('current commentary score: ',score)
                total_score += score['sentiment_score'] if score['sentiment_score'] != None else 0
                size += 1


            print('total_score: ', total_score)
            if size > 0:
                postScore = total_score / size
            print('num of comments: ',len(comments))
            print('postScore: ',postScore)

            if postScore != oldPostScore:
                postId = str(post_id)
                url = 'http://tip-laravel.herokuapp.com/api/post/'+ postId +'/edit'
                json = {
                    'sentiment_score': postScore,
                }
                x = requests.put(url, json = json)
                print(x.text)
       
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            if len(post) > 0:
                result = {
                    "post_score": postScore,
                    # "comment_score": sentimentFiltered['sentiment_score']
                }
            else:
                result = {
                    "error": "Post não encontrado"
                }
        return result
