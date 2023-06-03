import tweepy
from Keys import *
import pandas as pd
import textblob as tb
from utils import remove_emoji
import os

auth = tweepy.OAuthHandler(API_KEY,API_KEY_SECRET) 

auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

user = "lucasAvilss"
limit = 1000

tweets = tweepy.Cursor(api.user_timeline,screen_name = user,count = 200, tweet_mode='extended').items(limit)

columns =['tweet','Polaridade','Subjetividade']
data = []

for tweet in tweets:
    text = tweet.full_text
    print(text)
    text = remove_emoji(text)
    b = tb.TextBlob(text)
    try:
        b = b.translate(from_lang = 'pt',to='en')

    except tb.exceptions.NotTranslated:
        b = tb.TextBlob(text)
    
    finally:
        sent = b.sentiment
        polar = sent[0]
        subj = sent[1]
        
    data.append([text, polar, subj])
   



df = pd.DataFrame(data,columns=columns)


df.to_csv("tweets.csv",index=True)
