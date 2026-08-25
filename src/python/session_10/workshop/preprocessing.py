from config import drop_col

def drop_columns(df,columns):
    return df.drop(columns=columns)

def get_data_summery(df:pd.DataFrame):
    return pd.DataFrame({"Dtype ":df.dtypes,"N_unique ": df.nunique()})