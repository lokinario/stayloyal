import tweepy
import csv
import time
import webbrowser
# Credentials
import credentials as c
def main():
    auth = tweepy.OAuthHandler(c.CONSUMER_KEY, c.CONSUMER_SECRET)
    auth.set_access_token(c.ACCESS_TOKEN, c.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # values
    followers = list()
    friends = list()

    # get followers
    f = tweepy.Cursor(api.followers,count=200).items()
    for u in f:
        followers.append(u.screen_name)
    print(len(followers))

    users = tweepy.Cursor(api.friends, count = 200).items()
    for u in users:
        if (((u.followers_count < 1000) and (u.followers_count != 0))and not (u.verified)):
            friends.append(u.screen_name)
            #print(u.screen_name,u.followers_count)
        else:
            pass


    print(len(friends))

    snakes = list()
    bye = 0
    # check whos a snake
    for friend in friends:
        if friend not in followers:
            api.destroy_friendship(friend)
            bye = bye + 1

    status = "Unfollowed {} via stayloyal"
    api.status_update(status.format(bye))


if __name__ == "__main__":
    main()
