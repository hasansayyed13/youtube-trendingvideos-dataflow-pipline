from log import logger
import json
from datetime import date as dt
from config import raw_file_path



def load_data(response_data):
    logger.info(f"Loading Started")
    # Save the response data to a file
    try:
        file_name = raw_file_path
        with open(file_name, 'a') as file:
            json.dump(response_data, file)
            logger.info(f"Raw Data Saved As:{file_name}")
        return response_data
    except Exception as e:
        logger.info(f"Error :{e}")
        raise e


