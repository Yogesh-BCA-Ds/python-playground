'''
API -> JSON -> list+dict -> DataFrame 
'''
import requests
import pandas as pd
response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response.status_code) # if status is 200 then loaded successfully 
print()

data = response.json()
df0 = pd.DataFrame(data)
print(df)
print(df0['address'][0])
print(df0['address'][0]['street'][2])
print(df0['address'][0]['street'])


