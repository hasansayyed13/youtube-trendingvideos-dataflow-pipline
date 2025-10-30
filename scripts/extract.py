import requests
import json
from datetime import date as dt
from log import logger
from config import api_key



def extract_data(url:str,region_code:str,maxium_result:int):
    # Set the parameters for the API request
    params={
        'part':'snippet,statistics,contentDetails',
        'chart':'mostPopular',
        'regionCode':region_code,
        'maxResults':maxium_result,
        'key':api_key
    }
    try:
        # Make the API request
        response=requests.get(url,params=params)
        # Check if the request was successful or Not
        logger.info(f"STATUS ::{response.raise_for_status()}")
        #Check Data found
        logger.info(f"TOTAL DATA FOUND ::{len(response.json()['items'])}")

        return response.json()
    except Exception as e:
        logger.info(f"Error:{e}")
        raise e


