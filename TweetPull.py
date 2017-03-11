import tweepy
from tweepy import OAuthHandler
import csv


#setting up the crawler

consumer_key = 'P571oNtviMC0bWNlQMBJKBHFG'
consumer_secret = 'Vjf9DAfHUOIh6UvA6kGf7rGtzk5DpWqmR88YINNQsX13Y4X0nb'
access_token = '252783837-ohazajCwKzGg5THuKYmRRjLBPglNJyQWGGb8ERIp'
access_secret = '4mWOGr2WpmBfXZMwcdEIKcB6rIB6gQgMVynO3knuGzO3q'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def get_tweets(username, tweetNumber):
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

    get_tweets('realDonaldTrump', 2)