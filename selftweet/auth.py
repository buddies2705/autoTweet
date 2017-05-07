import tweepy
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("/home/gauravagarwal/tweet_config.txt")


def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


class Auth:
    consumer_key = ConfigSectionMap("SectionOne")['consumer_key']
    consumer_secret = ConfigSectionMap("SectionOne")['consumer_secret']
    access_token = ConfigSectionMap("SectionOne")['access_token']
    access_token_secret = ConfigSectionMap("SectionOne")['access_token_secret']

    @staticmethod
    def get_auth():
        auth = tweepy.OAuthHandler(Auth.consumer_key, Auth.consumer_secret)
        auth.set_access_token(Auth.access_token, Auth.access_token_secret)
        return auth

    @staticmethod
    def get_api():
        return tweepy.API(Auth.get_auth())
