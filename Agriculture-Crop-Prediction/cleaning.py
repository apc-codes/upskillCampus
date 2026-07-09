def clean(df):
    df.drop_duplicates(inplace=True)
    df.fillna(0,inplace=True)
    return df
