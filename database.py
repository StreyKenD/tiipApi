import psycopg2
from config import config
# from sentimentAnalysis import get_sentiments_allb
import requests

def doQuery(payload, sentimentFiltered):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        selectPost = "select * from comments where post_id = %s;"
        cur.execute(selectPost, (payload['post_id'],))
        post = cur.fetchall()
        oldPostScore = post[6]  

        query = "select * from comments where post_id = %s;"
        cur.execute(query, (payload['post_id'],))
        comments = cur.fetchall()  
        total_score=sentimentFiltered['sentiment_score']
        size=0

        for comment in comments:
            total_score += comment[2] if comment[2] != None else 0
            size += 1

        postScore = total_score / size

        if postScore != oldPostScore:
            postId = str(post[0])
            url = 'http://tip-laravel.herokuapp.com/api/post/'+ postId +'/edit'
            json = {
                'sentiment_score': postScore,
            }
            x = requests.put(url, json = json)
            print(x.text)

        # chamar api do site /api/post/[ID]/edit
       
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


# def doQueryAllPosts():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         params = config()
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()

#         query = "select * from posts;"
#         cur.execute(query)
#         posts = cur.fetchall()  

#         for post in posts:
#             # print('postID', post[1])
#             total_score = 0
#             oldPostScore = post[6]
#             postScore = 0
#             size=0

#             query = "select * from comments where post_id = %s;"
#             cur.execute(query, (post[0],))
#             comments = cur.fetchall()  
#             for comment in comments:
#                 comment_analised = get_sentiments_all(comment)
#                 print(comment_analised)
#                 total_score += comment_analised['sentiment_score'] if comment_analised['sentiment_score'] != None else 0
#                 size += 1

#             if (size > 0):
#                 postScore = total_score / size


#             if postScore != oldPostScore:
#                 postId = str(post[0])
#                 url = 'http://tip-laravel.herokuapp.com/api/post/'+ postId +'/edit'
#                 json = {
#                     'sentiment_score': postScore,
#                 }
#                 x = requests.put(url, json = json)
#                 print(x.text)

#                 # chamar api do site /api/post/[ID]/edit
       
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')