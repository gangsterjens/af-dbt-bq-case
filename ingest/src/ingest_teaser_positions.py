import pandas as pd
import json
from pathlib import Path

   

def get_tp():
    BASE_DIR = Path(__file__).resolve().parent.parent  # = dn-case/
    DATA_DIR = BASE_DIR / "Data"
    path = DATA_DIR / "teaser_positions.json"
    with open(path, 'r') as f:
        data = json.load(f)

    df_t = pd.DataFrame(data)
    df_t
    return df_t

