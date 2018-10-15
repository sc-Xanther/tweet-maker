import tweepy
import pandas as pd
import numpy as np

import unidecode
import csv

import tensorflow as tf
tf.enable_eager_execution()
import time
import string

## Authenticate account
consumer_key = ''
consumer_secret = ''

access_key = ''
access_secret = ''

## Pull tweets using tweepy

def get_all_tweets(name):
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  api =tweepy.API(auth)
  
  all_tweets = []
  
  tweetTMP = api.user_timeline(screen_name = name, count = 200)
  all_tweets.extend(tweetTMP)
  
  oldest = all_tweets[-1].id - 1
  
  while len(tweetTMP) > 0:
    print('pulling tweets %s' % (oldest))
    
    tweetTMP = api.user_timeline(screen_name = name, count = 200)
    all_tweets.extend(tweetTMP)
    oldest = all_tweets[-1].id - 1
    
    print('%s tweets so far' % (len(all_tweets)))
    
  tweets = [[tweet.text.encode('utf-8')] for tweet in all_tweets]
  
  with open('%s.csv' % name, 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(tweets)

## Pull tweets for who?
get_all_tweets('USERNAME') ## this should be the twitter handle

## Generate the dataset

dataset = pd.read_csv(data.csv') ## use the csv name from above

dataset.columns = ['tweet']
dataset['tweet'] = dataset['tweet'].map(lambda x: x.strip('b"'))
dataset['tweet'] = dataset['tweet'].map(lambda x: x.strip('"'))
dataset['tweet'] = dataset['tweet'].map(lambda x: x.strip("'"))
dataset['tweet'] = dataset['tweet'].map(lambda x: x.split('https:')[0])
