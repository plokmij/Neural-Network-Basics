import tweepy
from textblob import TextBlob
f = open('tweets','w')
consumer_key = "xxxxxxxxxx"
consumer_secret = "QwxxxxxxxxxxxxxxxxkSxxxxx"
access_token = "10xxxxxxxxxxxxxxxxxxxx"
access_token_secret = "xxxxxxxxxxxxxxxxxxx"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#api.update_status('Hello Tweepy!')
public_tweets = api.search('Atleti')

for tweet in public_tweets:
    #f.write(tweet.text+",")
    print(tweet.text.encode('utf-8'))
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
