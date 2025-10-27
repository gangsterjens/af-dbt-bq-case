import pandas as pd

# Les gzip-fil
def load_file_from_gzip(path):
    df = pd.read_csv(path, compression="gzip")
    return df


