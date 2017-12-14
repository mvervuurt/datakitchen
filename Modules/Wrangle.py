import pandas as pd

def summary(pands_df):
    print(pands_df.shape)
    print(pands_df.dtypes)
    print(pands_df.describe())
    pands_df.head()