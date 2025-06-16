import requests
import json
import pandas as pd
import sqlite3



endpoint= "https://api.opendota.com/api"
params = {}
headers = {}

match_id = "8335179729"

match_data = requests.get(f"{endpoint}/matches/{match_id}", params=params, headers=headers).json()


with open(match_id + '.json' , 'w') as f:
    json.dump(match_data['players'], f, indent=4)


data_frame = pd.DataFrame(match_data['players'])

# Flatten or convert list/dict columns to JSON strings
for column in data_frame.columns:
    if data_frame[column].apply(lambda x: isinstance(x, (list, dict))).any():
        data_frame[column] = data_frame[column].apply(json.dumps)


print(data_frame)

connection = sqlite3.connect(f'{match_id}.db')

# Write the DataFrame to an SQLite table
data_frame.to_sql('players', connection, if_exists='replace', index=False)

# Close the connection
connection.close()

print("DataFrame successfully saved to SQLite database!")
