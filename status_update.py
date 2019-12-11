import tweepy
import sys
# Credentials
import credentials as c


def main():
    if (len(sys.argv) < 2):
        tweet = input("What's on your mind? ")
    else:
        # p = 0
        # while (p < len(sys.argv) - 1):
        #     print("parameter %i: %s" % (p, sys.argv[p])
        #     p = p + 1
        #     # tweet += sys.argv[p]
        tweet = ''
        for i in sys.argv[1:]:
            tweet += i + ' '

    auth = tweepy.OAuthHandler(c.CONSUMER_KEY, c.CONSUMER_SECRET)
    auth.set_access_token(c.ACCESS_TOKEN, c.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    api.update_status(tweet)
    # print(tweet)


if __name__ == "__main__":
    main()
