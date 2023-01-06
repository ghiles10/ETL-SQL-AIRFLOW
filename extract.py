import tweepy

def extract_tweet(user = 'elonmusk')  : 

    """ allows you to retrieve all the data related to the user account and to store the data as a dictionary """

    access_key = "PiZ9HwCmjN9NUkdxGdabbHVSV" 
    access_secret = "TkxotsQVGI6zErHNDeKkpKBttPtKCICxfQTfKxWHkR8b1yCYiC" 
    consumer_key = "1572886741-D4cmA6kTxR3ctyHC54CP8S5TddMe8WNcPW59xR4"
    consumer_secret = "lf03CiqS2ECm6vkgDPlmlSVHQ3BxoIU9zqgaoFbxg3wyX"

    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)   
    auth.set_access_token(consumer_key, consumer_secret) 

    # Creating an API object 
    api = tweepy.API(auth)

    # store info 
    infos = {
        user: {
            "TWEET_INFO": {
                "text": [] ,
                "favorite_count":[] ,
                "retweet_count": [],
                "created_at":[]
            },
            "USER_INFO": {
                "followers_count":'' ,
                "following_count": '',
                "created_at":'' ,
                "description":'' , 
                "location":''
            },
            "USER_ACTIVITY": {
                "favoris_count":'' ,
                "retweet_count":'' ,
            }
        }
    }

    # get user tweets 
    tweets = api.user_timeline(screen_name='@'+str(user), 
                            count=100,
                            include_rts = False,
                            tweet_mode = 'extended') 

    # retrieves tweets
    for tweet in tweets : 
        infos[user]["TWEET_INFO"]['text'].append(tweet._json["full_text"])
        infos[user]["TWEET_INFO"]['favorite_count'].append(tweet.favorite_count)
        infos[user]["TWEET_INFO"]['retweet_count'].append(tweet.retweet_count)
        infos[user]["TWEET_INFO"]['created_at'].append(tweet.created_at)
  
    # Retrieving account information
    user = api.get_user( screen_name = user)
    
    infos[user]["USER_INFO"]['followers_count'].append( user.followers_count)
    infos[user]["USER_INFO"]['following_count'].append( user.friends_count)
    infos[user]["USER_INFO"]['created_at'].append(user.created_at)
    infos[user]["USER_INFO"]['description'].append(user.description)
    infos[user]["USER_INFO"]['location'].append(user.location)


    # Retrieving activity account information
    user = api.get_user( screen_name = user)
    
    infos[user]["USER_ACTIVITY"]['favoris_count'].append( user.followers_count)
    infos[user]["USER_ACTIVITY"]['retweet_count'].append( user.friends_count)

    return infos     


