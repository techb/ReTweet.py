import tweepy
import json
import sys

# the Id of the user we are going to retweet from
who_to_retweet = "1336100553898733569"

# grab the credentials and auth our script
creds = json.loads( open("creds.json", "r").read() )
auth = tweepy.OAuthHandler(creds["api_key"], creds["api_secret"])
auth.set_access_token(creds["access_token"], creds["access_secret"])

# the twitter instance
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#make sure we can log in
try:
    api.verify_credentials()
    print("We're in")
except:
    print("We are not in...")
    sys.exit()


# Stream class that listens for tweets, then retweets them
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name} : {tweet.text} : {tweet.id}")
        try:
            api.retweet(tweet.id)
        except:
            print("Already posted")

    def on_error(self, status):
        print("Error detected")

# do the things and wait forever
tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(follow=[who_to_retweet])