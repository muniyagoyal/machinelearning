import tweepy
consumer_key="csq3vPzx5gP8YjfhY3xLAlonB"
consumer_secret="ZmC3qfJhtGscFnRyXeYJEW6QqD9gVhxeWMh3Tmj1V6VN86cv5v"
access_key="1081746680020520966-b9fwuN3esVy6l3kbPE1D2XqYWJyGUX"
access_secret="nM4P6e4WaPKeiUHtYFss5yqCBBQVGBVCoKLHUUHLT8TbW"

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

