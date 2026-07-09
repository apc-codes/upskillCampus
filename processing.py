import pandas as pd

def preprocess(df):
    df = df.drop_duplicates()
    df.fillna(method='ffill', inplace=True)
    return df
