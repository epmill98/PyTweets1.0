import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

def OAuth():
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_secret)
		return auth
	except Exception as e:
		return None

oauth = OAuth()
api = tweepy.API(oauth)

api.update_status('Hello World! (Created from my PyTweets1.0 Application)')