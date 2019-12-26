import tweepy
import logging
from config import create_api
import time
from download_t import download_img,tweet_media,tweet_utube
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def Mention(api,since_id):

    logger.info("Collecting info")

    new_since_id = since_id

    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():

        new_since_id = max(tweet.id, new_since_id)

        if tweet.in_reply_to_status_id is not None:

            status_id = tweet.in_reply_to_status_id
            tweet_u = api.get_status(status_id,tweet_mode='extended')

            print(tweet_u.full_text)

            if "media" in tweet_u.entities:

                expand_url = tweet_u.entities["media"][0]["expanded_url"]
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
                    download_img(tweet_u)

            elif "urls" in tweet_u.entities:

                if len(tweet_u.entities["urls"]) ==1:
                    vid_url = tweet_u.entities["urls"][0]["expanded_url"]
                    if re.match(r"https://www.youtube.com",vid_url):
                        try:
                            tweet_utube(vid_url)

                        except:
                            print("connection error")

            # api.update_status(
            #     status = "Nice one",
            #     in_reply_to_status_id = tweet.id
            # )

    return new_since_id

def main():
    api = create_api()
    since_id = 1206662450784944136
    while True:
        print(since_id)
        since_id = Mention(api,since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()