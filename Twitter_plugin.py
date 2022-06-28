import requests
import tweepy
import pyopenfec                                             
import main
import FEC_plugin

from FEC_plugin import Check_funding

def Twitter_target():

    Client = tweepy.Client(bearer_token="foo",
        consumer_key="foo",
        consumer_secret="foo",
        access_token=None, access_token_secret=None, wait_on_rate_limit=True)


    Client.create_list(name="Politicians", description=None, private=True, user_auth=True)
    target = Client.get_user(id=None, username="tedcruz")       # expand for full list use, currently just Cruz
    Client.add_list_member("Politicians", target.id, auth=True)

# Only setup for specific ids at this time, expand to list and iterate through list.
#Outer for loop for list inclusion

    latest_Tweets = Client.get_users_tweets(target.id)        # returns last 10 tweets ids in a list
                                                             

    for i in range(len(latest_Tweets)):                       # iterate through latest_Tweets

        tweet_status = Client.get_status(latest_Tweets[i])
        favorited = tweet_status.favorited

        if (favorited == True):
            print("Tweet already favorited.")
        else:
            Top_funders = Check_funding()                     # calls FEC API, currently setup to return list of 5.
            message = "The above politician is funded by the following people:" "\n 1: " << Top_funders[0] << "\n 2: " << Top_funders[1] << "\n 3: " << Top_funders[2] << "\n 4: " << Top_funders[3] << "\n 5: " << Top_funders[4]

            Client.create_tweet(text=message, in_reply_to_tweet_id=latest_Tweets[i])

            Client.like_tweet(latest_Tweets[i])
            print("Tweet now liked.")
