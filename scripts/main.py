from extract import extract_data
from load import load_data
from transform import transform_data
from config import url,region_code,maximum_result
from log import logger

def run_pipeline():
    try:
        url_path=url
        r_code=region_code
        m_result=maximum_result
        logger.info("YOUTUBE-PIPLINE-STARTED")
        e_pipline=extract_data(url_path,r_code,m_result)
        l_pipline=load_data(e_pipline)
        transform_data(l_pipline)
        logger.info(f"YOUTUBE-PIPLINE-COMPLETED")
    except Exception as e:
        logger.error(f"YOUTUBE-PIPLINE-FAILED::{e}")
        raise e



if __name__ == "__main__":
    run_pipeline()
