import json
import os

config_f=os.path.join(os.path.dirname(__file__),
                      r"D:\youtube elt project\youtube-trendingvideos-dataflow-pipline\.idea\config.json")

with open(config_f,'r') as f:
    cfg=json.load(f)

API_KEYS=cfg.get('API_KEY')
MONGO__URL=cfg.get('MONGO_URL')
