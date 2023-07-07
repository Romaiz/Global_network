import pandas as pd
from Script_1 import csv_to_json

df = pd.read_csv('world_population.csv')
df2 = pd.read_csv('GEODATASOURCE-COUNTRY-BORDERS.csv')

df.rename(columns={'Country/Other': 'country_name'}, inplace=True)
df.drop(df.columns.difference(
    ['country_name', 'Population (2020)']), axis=1, inplace=True)
print(df.head())

merged_df = df2.merge(df, on='country_name', how='left')
print(merged_df.head())
merged_df['Population (2020)'].fillna(397628, inplace=True)
# merged_df.dropna(axis=1, inplace=True)
print(merged_df.head())
merged_df.to_csv('global_network.csv', index=False)
csvFile = "global_network.csv"
jsonFile = "global_network.json"
csv_to_json(csvFile, jsonFile)
