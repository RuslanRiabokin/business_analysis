import pandas as pd

df = pd.read_csv('file_2.csv')

# print(df.describe())
print(df.columns)
# print(df[['moderator', 'id_request']].head())
print(df.start_time.head())