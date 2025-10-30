import logging

logging.basicConfig(
    filename='E:\youtube-trendingvideos-dataflow-pipline\logs\youtube-etl-pipeline.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)