import tweepy
import pandas as pd
consumer_key ='c2TJKoMkL8KQxCVObTQWrNRHD'
consumer_secret ='Trie1n70yxYtihjA3hj8adWjS7VplJnLVOhNkj8xbHqXl0tvCQ'
access_token ='1386722037629030402-rGEFt594dO9bfErkyuliKNv3Hbyz0P'
access_token_secret='c3R7K3X7XUN9RxiFqVQ82ytF8gEDb1xVXgpGTpqOOEL54'
callback_uri='oob'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret,callback_uri)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
number_of_tweets =20
tweets=[]
likes=[]
time=[]

for i in tweepy.Cursor(api.search,q='Bitcoin',tweet_mode="extended").items(number_of_tweets):
	tweets.append(i.full_text)
	likes.append(i.favorite_count)
	time.append(i.created_at)
df=pd.DataFrame({'tweets':tweets,'likes':likes,'time':time})

df=df[~df.tweets.str.contains("RT")]
df=df.reset_index(drop=True )
print(df)
mostlike=df.loc[df.likes.nlargest(5).index]
print(mostlike)