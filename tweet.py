#!usr/bin/env python3
import tweepy
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from  nltk.stem import WordNetLemmatizer
from  nltk.corpus   import  stopwords
from nltk.probability import FreqDist
#from collections import Counter
import matplotlib.pyplot as plt
import string
consumer_key="csq3vPzx5gP8YjfhY3xLAlonB"
consumer_secret="ZmC3qfJhtGscFnRyXeYJEW6QqD9gVhxeWMh3Tmj1V6VN86cv5v"
access_key="1081746680020520966-b9fwuN3esVy6l3kbPE1D2XqYWJyGUX"
access_secret="nM4P6e4WaPKeiUHtYFss5yqCBBQVGBVCoKLHUUHLT8TbW"

def get_tweets(topic):
	#authenticating twitter with consumer key and consumer  secret
	auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
	#setting access token
	auth.set_access_token(access_key,access_secret)
	#connecting bssetting access tokenpi
	api=tweepy.API(auth)
	#number_of_tweets=50
	tweets=api.search(q=topic,count=10)
	tmp=[]
	tmp1=[]

	tweets_for_csv=[tweet.text for tweet in tweets]
	for j in tweets_for_csv:
		tmp.append(j)
	print("################################EXTRACTED TWEETS")
	print(tmp)
	print("####################################LEMMATIZED TWEETS")
	#lemmatization
	lemma=WordNetLemmatizer()
	for i in range(len(tmp)):
		words=word_tokenize(tmp[i])
		newword=[lemma.lemmatize(word) for word in words]
		tmp[i]=' '.join(newword)
	print(tmp)
	tmp1=tmp
	print("########################REMOVED STOP WORDS & SPECIAL CHARACTERS")
	# removing  stopwords and special characters
	for  j  in  range(len(tmp)):
		words=word_tokenize(tmp[j])
		newword1=[word for word  in  words if word not in (stopwords.words('english') and string.punctuation) ]
		tmp1[j]=' '.join(newword1)
	print(tmp1)
	#removing special characters
	'''
	for j in range(len(tmp1)):
		words=word_tokenize(tmp[j])
		nw=[word for word in words if word not in string.punctuation]
		tmp1[j]=' '.join(nw)
	print("#############################AFTER REMOVING SPECIAL CHARACTERS")
	print(tmp1)
	'''
	#counting frequent words
	fdist=FreqDist()
	w1=[]#list to store common words
	f1=[]#list to store frequencies fo that word

	for k in range(len(tmp1)):
		words=word_tokenize(tmp1[j])
		for word in words:
			fdist[word.lower()] += 1
	for word,freq in fdist.most_common(20):
		w1.append(word)
		f1.append(freq)
	print(w1,f1)
	'''	
	for k in range(len(tmp1)):
		words=word_tokenize(tmp1[k])
		count=Counter(words)
	most_occur=count.most_common(12)	
	for i in range(len(most_occur)):
		w1.append(most_occur[i][0])
		f1.append(most_occur[i][1])
	'''
	plt.xlabel("Words")
	plt.ylabel("Occurance")
	y_pos = range(len(w1))
	plt.bar(y_pos, f1)
	# Rotation of the bars names
	plt.xticks(y_pos, w1, rotation=90)
	plt.show()

		

if __name__=='__main__':
	data=input("Enter topic: ")
get_tweets(data)
'''
import sys
topic=sys.argv(1)  then run using python3 tweet.py virat
'''

