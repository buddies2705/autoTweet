import tweepy
from tweepy import TweepError

from auth import Auth
from tweetStreamListner import TweetStreamListner


def main():
    try:
        go_stream()
    except TweepError:
        print "Exception"
    except BaseException:
        print "Exception"
    finally:
        go_stream()


def go_stream():
    tweet_stream_listner = TweetStreamListner
    stream = tweepy.Stream(auth=Auth.get_auth(), listener=tweet_stream_listner())
    print "starting"
    stream.filter(languages=["en"], track=['java', 'nerd', 'geek', 'spring-web', 'language', 'Hacker']
                  , filter_level='medium')


if __name__ == "__main__":
    main()
