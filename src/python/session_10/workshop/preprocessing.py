import pandas as pd

def drop_columns(df, columns):
    return df.drop(columns=columns)
def get_data_summary(df: pd.DataFrame)->pd.DataFrame:
        
    return pd.DataFrame({"Dtypes ": df.dtypes, "N_unique ":df.n_unique}).T