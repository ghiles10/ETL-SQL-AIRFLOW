import tweepy
import pandas as pd 


access_key = "PiZ9HwCmjN9NUkdxGdabbHVSV" 
access_secret = "TkxotsQVGI6zErHNDeKkpKBttPtKCICxfQTfKxWHkR8b1yCYiC" 
consumer_key = "1572886741-D4cmA6kTxR3ctyHC54CP8S5TddMe8WNcPW59xR4"
consumer_secret = "lf03CiqS2ECm6vkgDPlmlSVHQ3BxoIU9zqgaoFbxg3wyX"


# Twitter authentication
auth = tweepy.OAuthHandler(access_key, access_secret)   
auth.set_access_token(consumer_key, consumer_secret) 


## Creating an API object 
api = tweepy.API(auth)
tweets = api.user_timeline(screen_name='@elonmusk', 
                        # 200 is the maximum allowed count
                        count=200,
                        include_rts = False,
                        # Necessary to keep full_text 
                        # otherwise only the first 140 words are extracted
                        tweet_mode = 'extended'
                        )
print(type(tweets))