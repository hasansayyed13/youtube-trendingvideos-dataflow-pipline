import requests
import json
from config import API_KEYS


def extract_data(region="IN"):
    URL= r"https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "snippet,statistics",
        "chart": "mostPopular",
        "regionCode": region,
        "maxResults": 50, # CHANGE IF YOU WANT TO CHANGE  YOU CAN  i.e 100 TRENDING VDIEOS DATA
        "key": API_KEYS  #PUT YOU API KEY HERE DIRECT OR USE CAN IMPORT FROM OTHER FILE TOO
    }
    result = requests.get(URL, params=params)
    raw_data= result.json()

    return raw_data
