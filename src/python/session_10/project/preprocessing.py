import pandas as pd
import os

def Read_data_file(file_path):
    if not os.path.exists(file_path):
        print("The file does not exist.")
        return None
    elif not os.path.isfile(file_path):
        print("The provided path is invalid.")
        return None
        
    try:
        df = pd.read_csv(file_path)
        print("the file loaded successfully.")
        return df
    except FileExistsError as e:
        print(f"Error: {e}")
        
def Drop_unnecessary_features(df, cols_to_drop):
    df = df.drop(cols_to_drop,axis=1)
    return df

def Check_data_type(df):
    result= pd.DataFrame(
        {
            "Columns" :df.columns,
            "Type":df.dtypes,
            "U_Values":df.nunique()
        }
    )
    
    return result.to_string(index=False)