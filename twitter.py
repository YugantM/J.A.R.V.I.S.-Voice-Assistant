import tweepy


def login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    ret = {}
    ret['api'] = api
    ret['auth'] = auth
    return api


def post_tweets():
    consumer_key = 'Io9aj4<masked>NVuQzaGuK'
    consumer_secret = 'zIL28GWqGXD30<masked>gj5SiNcizRcA98S0JXTD'
    access_token = '2596662433-v6a58J7OG<masked>lVVO5kLkiuyUU47'
    access_token_secret = 'jjOlmFW8rGVtST<masked>4LCV8PFHfsfYuHZ9V'

    message = "this is a test tweet by BOT"

    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret)

    ret = api.update_status(status=message)


if __name__ == '__main__':
    post_tweets()
