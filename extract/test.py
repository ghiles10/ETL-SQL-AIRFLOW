USER_KEY = { 
        "access_key" : "PiZ9HwCmjN9NUkdxGdabbHVSV" ,
        "access_secret" : "TkxotsQVGI6zErHNDeKkpKBttPtKCICxfQTfKxWHkR8b1yCYiC" ,
        "consumer_key" : "1572886741-D4cmA6kTxR3ctyHC54CP8S5TddMe8WNcPW59xR4",
        "consumer_secret" : "lf03CiqS2ECm6vkgDPlmlSVHQ3BxoIU9zqgaoFbxg3wyX" 
} 


DB_DETAILS = {
            'db_name': 'mysql',
            'db_user': '139.99.209.131',
            'db_host': 'retail_db',
            'db_pass': ''
}  


OK = 'ok'

from utils import connection_object
conn = connection_object() 
cur = conn.cursor()

# cur.execute("""
#     SELECT table_name
#     FROM information_schema.tables
#     WHERE table_schema = 'public'
#     """)

# # Store the list of tables
# tables = cur.fetchall()
# # Iterate through the list of tables and drop each one
# for table in tables:
#     cur.execute(f"DROP TABLE {table[0]}")
#     print(table)
    
# conn.commit()
# conn.close()

cur.execute("""
    SELECT *
    FROM TWEET_INFO
    """)

# Store the list of tables
tables = cur.fetchall()
# Iterate through the list of tables and drop each one
for table in tables:
    # cur.execute(f"DROP TABLE {table[0]}")
    print(table)
    
conn.commit()
conn.close()
