# Tweets_Funded_By
Twitter Bot for Election Transparency

This twitter bot uses Python scripts to make calls to the Twitter API using Tweepy.
Once Tweepy finds the latest 10 tweets from Federal Politicians, it calls a custom Python wrapper pyopenfec.
Pyopenfec calls the FEC API and retrieve candidate data.
The top 5 individual donors are then returned to the twitter script.
Which then posts the reply to the original tweets with the top 5 individual donors that have paid the politician.

At this time, none of the project code is to be copied or reused.
