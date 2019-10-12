from os import getenv
from dotenv import load_dotenv
import tweepy

load_dotenv()

API_KEY = getenv('API_KEY')
API_SECRET_KEY = getenv('API_SECRET_KEY')
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        print('*' * 40)
        print(status.text)
        print('*' * 40)

listener = Listener()
stream = tweepy.Stream(auth=api.auth, listener=listener)

stream.filter(track=['python'])
