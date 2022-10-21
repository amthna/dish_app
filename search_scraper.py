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
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://kooladmin:rnrMYhiEtPoRzl7X@cluster0.lrohczl.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["dish_app_db"]
mycol = mydb["countries"]

f = open('countries.json')
data = json.load(f)
for i in data.values():
    time.sleep(1)

    dish_dict = get_dishes(i)

    x = mycol.insert_one(dish_dict)
