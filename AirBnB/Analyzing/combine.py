import json
import urllib.request
import pandas as pd

Springdale = 'https://raw.githubusercontent.com/Reece323/air-scrape/main/AirBnB/Data/Springdale.json'
response = urllib.request.urlopen(Springdale)
Springdale = json.loads(response.read())

Springdale = pd.json_normalize(Springdale)
Springdale_amenities = Springdale['listingAmenities'].explode().apply(pd.Series)
Springdale_amenities.rename(columns={col:f'amenities_{col}' for col in Springdale_amenities.columns}, inplace=True)


cols = [col for col in Springdale.columns if col not in ['amenities_records']]
Springdale_df = Springdale[cols].join(Springdale_amenities)
Springdale_df.dropna(axis=1, how='all', inplace=True)

Bella_Vista = 'https://raw.githubusercontent.com/Reece323/air-scrape/main/AirBnB/Data/Bella_Vista.json'
response = urllib.request.urlopen(Bella_Vista)
Bella_Vista = json.loads(response.read())

Bella_Vista = pd.json_normalize(Bella_Vista)
Bella_Vista_amenities = Bella_Vista['listingAmenities'].explode().apply(pd.Series)
Bella_Vista_amenities.rename(columns={col:f'amenities_{col}' for col in Bella_Vista_amenities.columns}, inplace=True)


cols = [col for col in Bella_Vista.columns if col not in ['amenities_records']]
Bella_Vista_df = Bella_Vista[cols].join(Bella_Vista_amenities)
Bella_Vista_df.dropna(axis=1, how='all', inplace=True)

Bentonville_new = 'https://raw.githubusercontent.com/Reece323/air-scrape/main/AirBnB/Data/Bentonville_new.json'
response = urllib.request.urlopen(Bentonville_new)
Bentonville_new = json.loads(response.read())

Bentonville_new = pd.json_normalize(Bentonville_new)
Bentonville_new_amenities = Bentonville_new['listingAmenities'].explode().apply(pd.Series)
Bentonville_new_amenities.rename(columns={col:f'amenities_{col}' for col in Bentonville_new_amenities.columns}, inplace=True)


cols = [col for col in Bentonville_new.columns if col not in ['amenities_records']]
Bentonville_new_df = Bentonville_new[cols].join(Bentonville_new_amenities)
Bentonville_new_df.dropna(axis=1, how='all', inplace=True)

bentonville = 'https://raw.githubusercontent.com/Reece323/air-scrape/main/AirBnB/Data/Bentonville_all.json'
response = urllib.request.urlopen(bentonville)
Bentonville = json.loads(response.read())

Bentonville_json_normalize = pd.json_normalize(Bentonville)
Bentonville_amenities = Bentonville_json_normalize['listingAmenities'].explode().apply(pd.Series)
Bentonville_amenities.rename(columns={col:f'amenities_{col}' for col in Bentonville_amenities.columns}, inplace=True)


cols = [col for col in Bentonville_json_normalize.columns if col not in ['amenities_records']]
Bentonville_df = Bentonville_json_normalize[cols].join(Bentonville_amenities)
Bentonville_df.dropna(axis=1, how='all', inplace=True)

Fayetteville = 'https://raw.githubusercontent.com/Reece323/air-scrape/main/AirBnB/Data/Fayetteville_new.json'
response = urllib.request.urlopen(Fayetteville)
Fayetteville = json.loads(response.read())

Fayetteville = pd.json_normalize(Fayetteville)
Fayetteville_amenities = Fayetteville['listingAmenities'].explode().apply(pd.Series)
Fayetteville_amenities.rename(columns={col:f'amenities_{col}' for col in Fayetteville_amenities.columns}, inplace=True)


cols = [col for col in Fayetteville.columns if col not in ['amenities_records']]
Fayetteville_df = Fayetteville[cols].join(Fayetteville_amenities)
Fayetteville_df.dropna(axis=1, how='all', inplace=True)

Lowell = 'https://raw.githubusercontent.com/Reece323/air-scrape/main/AirBnB/Data/Lowell.json'
response = urllib.request.urlopen(Lowell)
Lowell = json.loads(response.read())

Lowell = pd.json_normalize(Lowell)
Lowell_amenities = Lowell['listingAmenities'].explode().apply(pd.Series)
Lowell_amenities.rename(columns={col:f'amenities_{col}' for col in Lowell_amenities.columns}, inplace=True)


cols = [col for col in Lowell.columns if col not in ['amenities_records']]
Lowell_df = Lowell[cols].join(Lowell_amenities)
Lowell_df.dropna(axis=1, how='all', inplace=True)

Rogers = 'https://raw.githubusercontent.com/Reece323/air-scrape/main/AirBnB/Data/Rogers.json'
response = urllib.request.urlopen(Rogers)
Rogers = json.loads(response.read())

Rogers = pd.json_normalize(Rogers)
Rogers_amenities = Rogers['listingAmenities'].explode().apply(pd.Series)
Rogers_amenities.rename(columns={col:f'amenities_{col}' for col in Rogers_amenities.columns}, inplace=True)


cols = [col for col in Rogers.columns if col not in ['amenities_records']]
Rogers_df = Rogers[cols].join(Rogers_amenities)
Rogers_df.dropna(axis=1, how='all', inplace=True)

df1 = pd.concat([Springdale_df, Bella_Vista_df], axis=0)

df2 = pd.concat([df1, Bentonville_new_df], axis=0)

df3 = pd.concat([df2, Bentonville_df], axis=0)

df4 = pd.concat([df3, Fayetteville_df], axis=0)

df5 = pd.concat([df4, Lowell_df], axis=0)

df = pd.concat([df5, Rogers_df], axis=0)
