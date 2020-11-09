import tweepy
import json
import webbrowser
# Credentials
import credentials as c


def main():
    callback_uri = 'oob'
    auth = tweepy.OAuthHandler(c.CONSUMER_KEY, c.CONSUMER_SECRET,callback_uri)
    redirect_url = auth.get_authorization_url()
    webbrowser.open(redirect_url)
    pin_input = input("What's the pin value? ")
    auth.get_access_token(pin_input)

    #auth.set_access_token(c.ACCESS_TOKEN, c.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # values
    followers = list()

    f = tweepy.Cursor(api.search,'python').items(10)
    for t in f:
        try:
            t.favorite()
        except: 
            print("too fast bucko")
            break
    


if __name__ == "__main__":
    main()
