from pytube import YouTube 
from twitterdl import TwitterDownloader
import re
import wget
import boto3
from datetime import datetime


s3 = boto3.client("s3")

def download_img(tweet):

    dir = "img/"
    img = tweet.entities["media"][0]["media_url"]
    img_path = wget.download(img,dir)
    s3.upload_file(str(img_path),"tutbot","-"+img_path.split("/")[-1])


def tweet_media(tweet_url):
    o = TwitterDownloader(tweet_url) 
    name, f_path = o.download()
    s3.upload_file(str(f_path),"tutbot",name)


def tweet_utube(tweet_url):
    yt = YouTube(tweet_url) 
    y = yt.streams.filter(progressive=True, file_extension='mp4')
    y = y.order_by('resolution')
    y = y.desc().first()
    vid_path = y.download("./output")
    now = str(datetime.now())
    now = "-".join(now.split(" "))
    s3.upload_file(str(vid_path),"tutbot", now+vid_path.split("/")[-1])
