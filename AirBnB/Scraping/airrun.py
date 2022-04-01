from airparser import Parser
import time
import datetime

if __name__ == "__main__":
    # parameterize dates
    date_1 = datetime.date.today() + datetime.timedelta(days=7)
    date_2 = datetime.date.today() + datetime.timedelta(days=14)
    date_1 = date_1.strftime('%Y-%m-%d')
    date_2 = date_2.strftime('%Y-%m-%d')

    # page_url = 'https://www.airbnb.com/s/Bentonville--Arkansas--United-States/homes?query=Bentonville%2C%20Arkansas%2C%20United%20States&checkin={date_1}&checkout={date_2}&adults=4'


    locations = {
        'Bentonville_Ar': f'https://www.airbnb.com/s/Bentonville--Arkansas--United-States/homes?query=Bentonville%2C%20Arkansas%2C%20United%20States&checkin={date_1}&checkout={date_2}&adults=4',
        }

    for location in locations:
        new_parser = Parser(locations[location], f'./Data/{location}.csv')
        t0 = time.time()
        new_parser.parse()
        print(location, time.time() - t0)