import tweepy
import time
# Credentials
import credentials as c
def main():
    auth = tweepy.OAuthHandler(c.CONSUMER_KEY, c.CONSUMER_SECRET)
    auth.set_access_token(c.ACCESS_TOKEN, c.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    tweet = input("What's on your mind? ")
    api.update_status(tweet)


if __name__ == "__main__":
    main()
