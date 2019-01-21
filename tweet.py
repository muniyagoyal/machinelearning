import tweepy
consumer_key=""
consumer_secret=""
access_key=""
access_secret=""

def get_tweets(username):
	auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_key,access_secret)
	api=tweepy.API(auth)
	number_of_tweets=50
	tweets=api.search(q=username,count=100)
	tmp=[]
	tweets_for_csv=[tweet.text for tweet in tweets]
	for j in tweets_for_csv:
		tmp.append(j)
	print(tmp)
	print(len(tmp))
if __name__=='__main__':
	data=input("Enter topic: ")
get_tweets(data)

