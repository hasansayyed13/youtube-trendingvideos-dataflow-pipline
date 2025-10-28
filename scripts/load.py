from pymongo import MongoClient
from extract import extract_data
from config import MONGO__URL
import json



def connect_to_mongo():
    print("------DATA EXTRACTED START------")
    JSON = extract_data()
    with open(r"D:\youtube elt project\youtube-trendingvideos-dataflow-pipline\raw_data\raw_json_data.json","w") as f:
        json.dump(JSON,f,indent=4)

    client = MongoClient(MONGO__URL)
    print("------CONNECT TO MongoDB------")
    db = client["Youtube_data"]
    collection = db["trending_video_data"]
    collection.insert_many(JSON['items'])
    print("----- DATA SUCCESSFULLY LOADED ------")


