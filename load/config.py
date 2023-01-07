from dotenv import load_dotenv
import os
load_dotenv(r'./.env')

USER_KEY = { 
        "access_key" : os.getenv("access_key")  ,
        "access_secret" : os.getenv("access_secret"),
        "consumer_key" : os.getenv("consumer_key"),
        "consumer_secret" : os.getenv("consumer_secret")
} 


DB_DETAILS = {
            'db_name': os.getenv("db_name"),
            'db_user': os.getenv("db_user"),
            'db_host': '0.0.0.0',
            'db_pass': os.getenv("db_pass")
} 

USER_NAME = 'elonmusk' 
