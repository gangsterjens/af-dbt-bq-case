import pandas as pd
import json
from pathlib import Path

   

def get_keywords():
    BASE_DIR = Path(__file__).resolve().parent.parent  # = dn-case/
    DATA_DIR = BASE_DIR / "Data"
    path = DATA_DIR / "keywords.json"
    with open(path, 'r') as f:
        data = json.load(f)


    kw_list = []
    lantern_ids = []

    for el in data:
        lantern_id = el.get('lantern_id')
        if lantern_id in lantern_ids:
            continue
        updated_date = el.get('updated_date')
        keywords = el.get('keywords')
        for kw in keywords:
            text = kw.get('text')
            kw_list.append(
                {'lantern_id': lantern_id,
                'updated_date': updated_date,
                'text': text})
        lantern_ids.append(lantern_id)


    df_kw = pd.DataFrame(kw_list)
    return df_kw

