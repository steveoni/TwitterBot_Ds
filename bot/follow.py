
import tweepy
import logging
from config import create_api
import json
from download_t import download_img,tweet_media,tweet_utube
import boto3
from urllib3.exceptions import ProtocolError
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class Monitor(tweepy.StreamListener):
    def __init__(self, api):
        super(tweepy.StreamListener, self).__init__()
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        
        logger.info(f"Processing tweet id {tweet.id}")
        logger.info(f"tweet {tweet.id}")

        
        print(tweet.text)
    

        if "media" in tweet.entities:

            expand_url = tweet.entities["media"][0]["expanded_url"]
            media_type = expand_url.split("/")[-2]
            print("expand_url", expand_url)
            if media_type == "video":

                print("video")
                try:

                    tweet_media(expand_url)
                except:
                    print("not a video url")
            else:
                print("media")
                download_img(tweet)

        elif "urls" in tweet.entities:

            if len(tweet.entities["urls"]) ==1:
                vid_url = tweet.entities["urls"][0]["expanded_url"]
                if re.match(r"https://www.youtube.com",vid_url):
                    try:
                        tweet_utube(vid_url)

                    except:
                        print("connection error")


    def on_error(self, status):
        logger.error(status)

def main():
    api = create_api()
    tweets_listener = Monitor(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    while True:
        try:

            stream.filter(follow=['1138739106031308800'], languages=["en"])
        except (ProtocolError,AttributeError):
            continue

if __name__ == "__main__":
    main()