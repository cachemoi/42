import tweepy
from tweepy import OAuthHandler
import csv
import time

#setting up the crawler

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit= True, wait_on_rate_limit_notify=True)


def get_tweets(username, tweetNumber, date):
    """

    :param username:
    The user you want to target
    :param tweetNumber:
     The number of tweets you want to pull
    :return:
    saves csv of tweets in the current directory in a tweets file
    """

    tweets = api.user_timeline(screen_name=username, count=tweetNumber)


    for tweet in tweets:
        print(tweet.created_at,tweet.text.encode("utf-8"))

    # create array of tweet information: username, tweet id, date/time, text
    csvTweets = [[username, tweet.id_str, tweet.created_at, tweet.text] for tweet in tweets]

    #create header for the csv
    csvHeader = ['user', 'tweetID', 'date', 'content']

    # write to a new csv file from the array of tweets
    "writing to {0}_tweets.csv".format(username)
    with open('tweets/' + "{0}_tweets.csv".format(username), 'w+', newline='') as file:
        writer = csv.writer(file, delimiter=',')

        writer.writerows([csvHeader])
        writer.writerows(csvTweets)

if __name__ == '__main__':

    for i in range(0,2):
        get_tweets('realDonaldTrump', 2)
        time.sleep(0.1)  # delays for 5 seconds
        get_tweets('realDonaldTrump', 2)