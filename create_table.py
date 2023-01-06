from utils import connection_object

def create_tables() : 

    conn = connection_object()
    cursor = conn.cursor()

    # create user info
    cursor.execute('''CREATE TABLE USER_INFO (user_name VARCHAR(20), followers INT, following INT, date_creation DATE)''')

    # create tweet info 
    cursor.execute('''CREATE TABLE TWEET_INFO (text VARCHAR, favorite_count INT, date_creation DATE, retweet_count INT)''')

    # create user activity 
    cursor.execute('''CREATE TABLE USER_ACTIVITY (favorite_count INT,retweet_count INT)''')

    conn.commit()
    cursor.close()
    conn.close()



if __name__ =='__main__' : 
    create_tables()

