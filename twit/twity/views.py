from django.shortcuts import render
from django.http import HttpResponse
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
number_of_tweets =50
tweets=[]
likes=[]
time=[]
s=[]
# Create your views here.
def home (request):
    return render(request,'home.html');
def add(request):
    tags=request.GET['tags'].strip()
    name=request.GET['name']
    tags=list(tags.split(' '))
    for i in tags:
        for i in tweepy.Cursor(api.search,q=i,tweet_mode="extended").items(number_of_tweets):
            if i.full_text[0]!='R':
                tweets.append(i.full_text)
                likes.append(i.favorite_count)
                time.append(i.created_at)
    return render(request,'s3.html',{'tweets':tweets,'likes':likes,'time':time,'name':name});