from config import*     # Contains API tokens
import tweepy
import json

# Initialize authentication to Twitter API
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, token_secret)

# Creates api object once auth is handled
api = tweepy.API(auth)

# Prints the latest 20 tweets on time line to x amt of characters?
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text, "\n")
# Follows users who are currently following the authenticated account(me)
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print(follower)





