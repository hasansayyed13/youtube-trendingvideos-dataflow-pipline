import json
from pymongo import MongoClient
import pandas as pd
from config import MONGO__URL


def transform_data():
    print("DATA NOW LOADING IN JSON FILE IN RAW_DATA FOLDER")
    with open(r"D:\youtube elt project\youtube-trendingvideos-dataflow-pipline\raw_data\raw_json_data.json",'r') as f:
        data = json.load(f)
    print("LOADING DONE")
    print("------IMPORTTANT DATA FETCHING AND CLEANING START-----")

    videos=[]

    for item in data['items']:
        video = dict(video_id=item['id'],
                     channel_Name=item['snippet']['channelTitle'],
                     video_title=item['snippet']['title'],
                     publishedTime=item['snippet']['publishedAt'],
                     views=int(item['statistics'].get('viewCount', 0)),
                     likes=int(item['statistics'].get('likeCount', 0)),
                     comments=int(item['statistics'].get('commentCount', 0)),
                     category=int(item['snippet']['categoryId']))
        videos.append(video)

    df = pd.DataFrame(videos)
    df.drop_duplicates(subset=['video_id'], inplace=True)
    df['publishedTime'] = pd.to_datetime(df['publishedTime'], errors='coerce')


    df.to_csv(r'D:\youtube elt project\youtube-trendingvideos-dataflow-pipline\clean data\clan_data.csv', index=False)
    print("-----DATA WAS CLEAN AND SAVE IN CLEAN DATA FOLDER FOR ANALYSIS-----")
    return df

