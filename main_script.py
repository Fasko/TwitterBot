from config import*     # Contains API tokens
import tweepy

# Initialize authentication to Twitter API
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, token_secret)

# Creates api object once auth is handled
api = tweepy.API(auth)

# Prints the latest 20 tweets on time line to x amt of characters?
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text, "\n")

