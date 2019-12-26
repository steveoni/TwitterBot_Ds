import tweepy
import logging
from config import create_api
import time
from download_t import download_img,tweet_media,tweet_utube
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def unroll_thread(tweet,api):
    
    text = []
    rep_status = tweet.in_reply_to_status_id
    user_id = tweet.in_reply_to_user_id
    
    def recur(rep_status):
        
#         print(rep_status)
        if rep_status == None:
            return 
        status = api.get_status(rep_status, tweet_mode='extended')
        text.append(status.full_text)
        
        rep_status = status.in_reply_to_status_id
        user2_id = status.in_reply_to_user_id
#         print(user_id,rep_status)
        if user_id == user2_id:
            recur(rep_status)
    recur(rep_status)
            
    return text[::-1]
        

def Thread_unroll(api,since_id):

    logger.info("Collecting info")

    new_since_id = since_id

    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():

        new_since_id = max(tweet.id, new_since_id)

        if tweet.in_reply_to_status_id is not None:

            text = unroll_thread(tweet,api)


            if len(text) > 1:
                name = tweet.id
                txt = open(f'{name}.txt','w+')
                text = "\n".join(text)
                txt.write(text)

    return new_since_id

def main():
    api = create_api()
    since_id = 1206662450784944136
    while True:
        print(since_id)
        since_id = Thread_unroll(api,since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()