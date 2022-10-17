# Import the beautifulsoup 
# and request libraries of python.
import json
from os import path
import requests
import bs4
import re
from result_scraper import result_scrape
from token_counter import token_counter
from get_dishes import get_dishes
import time

f = open('countries.json')
data = json.load(f)
for i in data.values():
    time.sleep(1)
    try:
        dish_data = get_dishes(i)

        filename = 'dish_dir/' + i + '.json'

        with open(filename, "w") as outfile:
            json.dump(dish_data, outfile)
        data = {}
    except:
        data = {}
        continue
