import random
import time

import tweepy

from auth import Auth


def retweet(status):
    api = Auth.get_api()
    api.retweet(status.id)
    wait()


def wait():
    t = random.randint(20, 60)
    print "waiting for " + str(t) + " seconds"
    time.sleep(t)


class TweetStreamListner(tweepy.StreamListener):
    def on_status(self, status):
        print status
        retweet(status)

    def on_exception(self, exception):
        print exception
        wait()
        pass

    def on_timeout(self):
        print "timeout"
        wait()
        pass

    def on_error(self, status_code):
        print status_code
        wait()
        pass
