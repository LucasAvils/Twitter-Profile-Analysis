import tweepy
from Keys import *
import pandas as pd

auth = tweepy.OAuthHandler(API_KEY,API_KEY_SECRET) 

auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

user = "lucasAvilss"
limit = 5000

tweets = tweepy.Cursor(api.user_timeline,screen_name = user,count = 200, tweet_mode='extended').items(limit)

columns =['user','tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name,tweet.full_text])

df = pd.DataFrame(data,columns=columns)

print(df)
