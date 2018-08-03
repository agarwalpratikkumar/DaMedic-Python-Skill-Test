import pandas as pd
import json

pd1 = pd.read_csv("data1.csv")
pd2 = pd.read_csv("data2.csv")

#Grouping data by key = 'id'
pd2.groupby(['id']).groups.keys()
grouped_data_tolist = pd.DataFrame(pd2.groupby('id')['value2'].apply(list))

#Merging both dataframes, producing output in json format
json_output = pd.merge(pd1, grouped_data_tolist, on=['id']).to_json(orient='records')

#Formatted json output by dumps
parsed = json.loads(json_output)
print(json.dumps(parsed, indent=2))
