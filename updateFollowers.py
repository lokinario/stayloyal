import tweepy
import json
# Credentials
import credentials as c
def main():
    auth = tweepy.OAuthHandler(c.CONSUMER_KEY, c.CONSUMER_SECRET)
    auth.set_access_token(c.ACCESS_TOKEN, c.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # values
    followers = list()

    # get followers
    f = tweepy.Cursor(api.followers,count=200).items()
    for u in f:
        followers.append(u.screen_name)

    data = {
        "followers":followers
    }
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
if __name__ == "__main__":
    main()
