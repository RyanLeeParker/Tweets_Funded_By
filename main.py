import requests
import tweepy
import PyOpenFec
import Twitter_plugin
import FEC_plugin
import time

from FEC_plugin import Check_funding            # function declaration
from Twitter_plugin import Twitter_target

while(True):

    Twitter_target()

    time.sleep(3600)                          # waits one hour


# Future additions
# Command shell options to add/remove/update Politicians list based on need.
# Would love to automate it, likely through FEC or 3rd party group.
