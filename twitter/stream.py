import tweepy
import configparser


config = configparser.ConfigParser()
config.read('conf.ini')
twitter_consumer_key = config['TWITTER']['twitter_consumer_key']
twitter_consumer_secret = config['TWITTER']['twitter_consumer_secret']
twitter_access_token = config['TWITTER']['twitter_access_token']
twitter_access_token_secret = config['TWITTER']['twitter_access_token_secret']

auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(vars(status))

    def on_error(self, status_code):
        if status_code == 420:
            return False


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(follow=follow_ids, async=True)
