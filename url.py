from locale import normalize
import pandas as pd

url = pd.read_csv('/Users/codyreece/Desktop/Repos/airbnb/air-scrape/Data/Bentonville_Ar.csv')


url_1 = url['url'].to_csv(r'./URLs1.csv', index = False)