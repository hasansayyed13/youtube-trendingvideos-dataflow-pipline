import pandas as pd
import numpy as np
from pymongo import MongoClient
import json
import requests


def youtube_data():
    region = input("Enter the region code: ")
    MAX_RESULTS = int(input("Enter the max results: "))
    URL = r"https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "snippet,statistics",
        "chart": "mostPopular",
        "regionCode": region,
        "maxResults": int(MAX_RESULTS), # CHANGE IF YOU WANT FIX NUMBER OF DATA i.e 100 TRENDING VDIEOS DATA
        "key": "ENTER YOU KEY HERE" #PUT YOU API KEY
    }
    result = requests.get(URL, params=params)
    JSON = result.json()
    data = json.dumps(JSON, indent=4)
    return JSON


def connect_to_mongo():
    JSON = youtube_data()
    client = MongoClient("mongodb://localhost:27017/")
    print("CONNECTING TO MONGO")
    db = client["Youtube_data"]
    collection = db["trending_video_data"]
    collection.insert_many(JSON['items'])



def clean_data():
    JSON = youtube_data()

    videos = []

    for item in JSON['items']:
        video = dict(video_id=item['id'],
                     channel_title=item['snippet']['channelTitle'],
                     title=item['snippet']['title'],
                     publishedTime=item['snippet']['publishedAt'],
                     views=int(item['statistics'].get('viewCount', 0)),
                     likes=int(item['statistics'].get('likeCount', 0)),
                     comments=int(item['statistics'].get('commentCount', 0)),
                     category=int(item['snippet']['categoryId']))
        videos.append(video)

    df = pd.DataFrame(videos)
    print(df)
    return df


if __name__ == '__main__':
    clean_data()
