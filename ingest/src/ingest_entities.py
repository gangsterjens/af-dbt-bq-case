import pandas as pd
import json
from pathlib import Path

   

def get_entities():
    BASE_DIR = Path(__file__).resolve().parent.parent  # = dn-case/
    DATA_DIR = BASE_DIR / "Data"
    path = DATA_DIR / "entities.json"
    with open(path, 'r') as f:
        data = json.load(f)
    lantern_ids = []
    ent_list = []
    for el in data:
        lantern_id = el.get('lantern_id')

        if lantern_id in lantern_ids:
            continue

        updated_date = el.get('updated_date')
        entities = el.get('entities')
        for en in entities:
            text = en.get('text')
            label = en.get('label')
            counts = en.get('counts')
            ent_list.append({
                'lantern_id': lantern_id,
                'updated_date': updated_date,
                'text': text,
                'label': label,
                'counts': counts
            })
        lantern_ids.append(lantern_id)

    df_ent = pd.DataFrame(ent_list)
    return df_ent

