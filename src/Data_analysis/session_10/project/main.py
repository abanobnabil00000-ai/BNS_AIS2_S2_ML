from Data_analysis.session_10.project.preprocessing import Read_data_file, Drop_unnecessary_features,Check_data_type
from Data_analysis.session_10.project.config.Config import cols_to_drop



path = input("inter the path: ")

df = Read_data_file(path)

if df is not None:
    print(Drop_unnecessary_features(df,cols_to_drop))
    print(Check_data_type(df))