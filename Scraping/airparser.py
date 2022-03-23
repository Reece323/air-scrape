import json
import os
import time
from multiprocessing import Pool

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BENTONVILLE_LINK = 'https://www.airbnb.com/s/Bentonville--Arkansas--United-States/homes?query=Bentonville%2C%20Arkansas%2C%20United%20States&checkin=2022-03-24&checkout=2022-03-31&adults=4'

RULES_SEARCH_PAGE = {
    'url': {'tag': 'a', 'get': 'href'},
    'name': {'tag': 'span', 'class': 'ts5gl90 tl3qa0j t1nzedvd dir dir-ltr'},
    'header': {'tag': 'div', 'class': 'cuu4odx c1frjvtt dir dir-ltr'},
    'guests': {'tag': 'span', 'class': 'mp2hv9t dir dir-ltr', 'order': 0},
    'rooms': {'tag': 'span', 'class': 'mp2hv9t dir dir-ltr', 'order': 1},
    'beds': {'tag': 'span', 'class': 'mp2hv9t dir dir-ltr', 'order': 2},
    'baths': {'tag': 'span', 'class': 'mp2hv9t dir dir-ltr', 'order': 3},
    'facilities': {'tag': 'div', 'class': 'i1wgresd dir dir-ltr', 'order': 1},
    'badge': {'tag': 'div', 'class': 'fcg8kp6 dir dir-ltr'},
    'rating': {'tag': 'span', 'class': 'rpz7y38 dir dir-ltr'},
    'review_count': {'tag': 'span', 'class': 'r1xr6rtg dir dir-ltr'},
    'price': {'tag': 'span', 'class': '_tyxjp1'},
}

RULES_DETAIL_PAGE = {
    'location': {'tag': 'span', 'class': '_8vvkqm3'},
    'specialties_1': {'tag': 'div', 'class': '_1qsawv5', 'order': -1},
    'host_joined': {'tag': 'li', 'class': '_194e2vt2', 'order': 1},
    'house_rules': {'tag': 'div', 'class': '_u827kd', 'order': 0},
}

def extract_listings(page_url, attempts=10):
    """Extracts all listings from a given page"""
    
    listings_max = 0
    listings_out = [BeautifulSoup('', features='html.parser')]
    for idx in range(attempts):
        try:
            answer = requests.get(page_url, timeout=5)
            content = answer.content
            soup = BeautifulSoup(content, features='html.parser')
            listings = soup.findAll("div", {"class": "cm4lcvy dir dir-ltr"})
        except:
            # if no response - return a list with an empty soup
            listings = [BeautifulSoup('', features='html.parser')]

        if len(listings) == 20:
            listings_out = listings
            break

        if len(listings) >= listings_max:
            listings_max = len(listings)
            listings_out = listings
            # print(listings_out)

    return listings_out


def extract_element_data(soup, params):
    """Extracts data from a specified HTML element"""
    
    # 1. Find the right tag
    if 'class' in params:
        elements_found = soup.find_all(params['tag'], params['class'])
    else:
        elements_found = soup.find_all(params['tag'])
        
    # 2. Extract text from these tags
    if 'get' in params:
        element_texts = [el.get(params['get']) for el in elements_found]
    else:
        element_texts = [el.get_text() for el in elements_found]
        
    # 3. Select a particular text or concatenate all of them
    tag_order = params.get('order', 0)
    if tag_order == -1:
        output = '**__**'.join(element_texts)
    else:
        output = element_texts[tag_order]
    # print(output)
    return output

# print('extract_listing_features')
def extract_listing_features(soup, rules):
    """Extracts all features from the listing"""
    features_dict = {}
    for feature in rules:
        try:
            features_dict[feature] = extract_element_data(soup, rules[feature])
        except:
            features_dict[feature] = 'empty'
    print(features_dict)
    return features_dict

# print('extract_soup_js')
def extract_soup_js(listing_url, waiting_time=[20, 1]):
    """Extracts HTML from JS pages: open, wait, click, wait, extract"""

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(options=options)

    # if the URL is not valid - return an empty soup
    try:
        driver.get(listing_url)
    except:
        print(f"Wrong URL: {listing_url}")
        return BeautifulSoup('', features='html.parser')
    
    # waiting for an element on the bottom of the page to load ("More places to stay")
    try:
        myElem = WebDriverWait(driver, waiting_time[0]).until(EC.presence_of_element_located((By.CLASS_NAME, '_4971jm')))
    except:
        pass

    # click cookie policy
    try:
        driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/section/footer/div[2]/button").click()
    except:
        pass
    # alternative click cookie policy
    try:
        element = driver.find_element_by_xpath("//*[@data-testid='main-cookies-banner-container']")
        element.find_element_by_xpath("//button[@data-testid='accept-btn']").click()
    except:
        pass

    # looking for price details
    price_dropdown = 0
    try:
        element = driver.find_element_by_class_name('_gby1jkw')
        price_dropdown = 1
    except:
        pass

    # if the element is present - click on it
    if price_dropdown == 1:
        for i in range(10): # 10 attempts to scroll to the price button
            try:
                actions = ActionChains(driver)
                driver.execute_script("arguments[0].scrollIntoView(true);", element);
                actions.move_to_element_with_offset(element, 5, 5)
                actions.click().perform()
                break
            except:
                pass
        
    # looking for amenities
    driver.execute_script("window.scrollTo(0, 0);")
    try:
        driver.find_element(by=By.PARTIAL_LINK_TEXT, value='amenities').click()
    except:
        pass # amenities button not found

    time.sleep(waiting_time[1])

    detail_page = driver.page_source
    # print(detail_page)

    driver.quit()

    return BeautifulSoup(detail_page, features='html.parser')

def scrape_detail_page(base_features):
    """Scrapes the detail page and merges the result with basic features"""
    
    detailed_url = 'https://www.airbnb.com' + base_features['url']
    soup_detail = extract_soup_js(detailed_url)

    features_detailed = extract_listing_features(soup_detail, RULES_DETAIL_PAGE)
    features_amenities = extract_amenities(soup_detail)

    features_detailed['amenities'] = features_amenities
    features_all = {**base_features, **features_detailed}
    # print(features_all)
    return features_all

def extract_amenities(soup):
    amenities = soup.find_all('div', {'class': '_gw4xx4'})
    
    amenities_dict = {}
    for amenity in amenities:
        # header = amenity.find('div', {'class': '_1crk6cd'}).get_text()
        # values = amenity.find_all('div', {'class': '_1dotkqq'})
        # values = [v.find(text=True) for v in values]
        amenities_all = [amenitie.text for amenitie in amenities]

        
        amenities_dict['amenities'] = amenities_all
        
    return json.dumps(amenities_dict)


class Parser:
    def __init__(self, link, out_file):
        self.link = link
        self.out_file = out_file

    
    def build_urls(self, listings_per_page=20, pages_per_location=15):
        """Builds links for all search pages for a given location"""
        url_list = []
        for i in range(pages_per_location):
            offset = listings_per_page * i
            url_pagination = self.link + f'&items_offset={offset}'
            url_list.append(url_pagination)
            self.url_list = url_list
            # print(self.url_list)


    def process_search_pages(self):
        """Extract features from all search pages"""
        features_list = []
        for page in self.url_list:
            listings = extract_listings(page)
            for listing in listings:
                features = extract_listing_features(listing, RULES_SEARCH_PAGE)
                features['sp_url'] = page
                features_list.append(features)

        self.base_features_list = features_list
        # print(self.base_features_list)
        

    def process_detail_pages(self):
        """Runs detail pages processing in parallel"""
        n_pools = os.cpu_count() // 2
        with Pool(n_pools) as pool:
            result = pool.map(scrape_detail_page, self.base_features_list)
        pool.close()
        pool.join()

        self.all_features_list = result
        print(self.all_features_list)

    def save(self, feature_set='all'):
        if feature_set == 'basic':
            pd.DataFrame(self.base_features_list).to_csv(self.out_file, index=False)
        elif feature_set == 'all':
            pd.DataFrame(self.all_features_list).to_csv(self.out_file, index=False)
        else:
            pass
        print('Saving pages...')
            
        
    def parse(self):
        self.build_urls()
        self.process_search_pages()
        self.process_detail_pages()
        self.save('all')


if __name__ == "__main__":
    new_parser = Parser(BENTONVILLE_LINK, './test.csv')
    t0 = time.time()
    new_parser.parse()
    print(time.time() - t0)
