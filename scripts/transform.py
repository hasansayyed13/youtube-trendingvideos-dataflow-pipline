import json
import pandas as pd
from log import logger
from config import clean_file_path


def transform_data(response_data):
    logger.info(f"Transforming Started")
    try:
        trending_data=response_data.get("items")
        videos =[
            {
                "video_id":data.get('id',None),
                "publishedAt":data.get("snippet", {}).get("publishedAt",None),
                "channelId":data.get("snippet", {}).get("channelId",None),
                "title":data.get("snippet", {}).get("title",None),
                "description":data.get("snippet", {}).get("description",None),
                "thumbnails":data.get("snippet", {}).get("thumbnails",{}).get("url",None),
                "channelTitle":data.get("snippet", {}).get("channelTitle",None),
                "tags":','.join(data.get("snippet", {}).get("tags",[])),
                "categoryId":data.get("snippet", {}).get("categoryId",None),
                "viewCount":data.get("statistics", {}).get("viewCount",None),
                "likeCount": data.get("statistics", {}).get("likeCount", None),
                "favoriteCount":data.get("statistics", {}).get("favoriteCount", None),
                "commentCount":data.get("statistics", {}).get("commentCount", None),

        }
             for data in trending_data
        ]

        df=pd.DataFrame(videos)

        # Remove Duplicates Value,NaN values and change column Data types
        df=(
            df
            .drop_duplicates(subset=['video_id'])
            .dropna(subset=['video_id','channelTitle','channelId'])
            .fillna({
                "viewCount": 0,
                "likeCount": 0,
                "favoriteCount": 0,
                "commentCount": 0

                 })
            .astype({
                "viewCount":int,
                "likeCount":int,
                "favoriteCount":int,
                "commentCount":int
                })
            )
        #convert date column into date format
        df['publishedAt']=pd.to_datetime(
            df['publishedAt'],
            format="mixed",
            errors='coerce'
        )
        #Assure that views data can't enter that have 0 views
        clean_df=df[df['viewCount']>0]
        #save into csv file
        try:
            file_name = clean_file_path
            clean_df.to_csv(clean_file_path, index=False)
            logger.info(f"Saved transformed data to {clean_file_path}")
        except Exception as e:
            logger.error(f"Error:{e}")
    except Exception as e:
        logger.info(f"Transforming Failed")
        raise e
