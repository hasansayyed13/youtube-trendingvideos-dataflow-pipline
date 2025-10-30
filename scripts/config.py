import json
from datetime import date as dt

#open json while those hold api_key
with open("api_key.json","r") as file:
        data=json.load(file)

api_key=data.get("api_key")
url = r"https://www.googleapis.com/youtube/v3/videos"
region_code = 'IN'
maximum_result= 50
raw_file_path=fr"..\raw_data\raw_trending_{region_code}_{dt.today().strftime('%Y%m%d')}_.json"
clean_file_path = fr"..\clean_data\raw_trending_{region_code}_{dt.today().strftime('%Y%m%d')}_.csv"
