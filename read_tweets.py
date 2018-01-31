from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import matplotlib.pyplot as plt



#Variables that contains the user credentials to access Twitter API
consumer_key = 'Io9aj4oEMo6NZPy1NVuQzaGuK'
consumer_secret = 'zIL28GWqGXD30vNoMUlxFqh16AgTX3gj5SiNcizRcA98S0JXTD'
access_token = '2596662433-v6a58J7OGe4eyKWWVjbSbCo6lVVO5kLkiuyUU47'
access_token_secret = 'jjOlmFW8rGVtSTe7Pfye7N2nwTla4LCV8PFHfsfYuHZ9V'


#This is a basic listener that just prints received tweets to stdout.
'''class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        file = open('twitter_data.txt', 'w')
        file.write(data)
        file.close()
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['ruby'])

'''

tweets_data_path = 'twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print(len(tweets_data))

print(tweets_data)

tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place']!=None else None, tweets_data)

tweets_by_lang = tweets['lang'].value_counts()

counts = tweets["country"].value_counts()
plt.bar(range(len(counts)), counts)
plt.show()

print(counts)

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang.plot(ax=ax, kind='bar', color='red')

