import json
from os import path
import requests
import bs4
import re
from result_scraper import result_scrape
from token_counter import token_counter

def get_dishes(country):
    nation = country
  
    # not a bot ;)
    headers = {
        'User-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
    }

    text= "+traditional+dishes"
    # url = 'https://google.com/search?q=' + nation + text

    q = nation + text

    params = {
      'q': q,  # query 
      'gl': 'us',    # country to search from
      'hl': 'en',    # language
    }

    request_result = requests.get("https://www.google.com/search", headers=headers, params=params)
      
    # Creating soup from the fetched request
    soup = bs4.BeautifulSoup(request_result.text,
                            "html.parser")

    # soup.find.all( h3 ) to grab 
    # all major headings of our search result,
    dish_results=soup.find_all( 'h3' )
    # links =  soup.find_all(('.yuRUbf a')['href'])
    # dish_results = soup.find_all("div", class_="yuRUbf")

    dishes = []

    # Iterate through the object 
    # and print it as a string.
    for dish in dish_results:
        link = dish.find_parent("a")

        url = re.search(r'url=(.*?)&amp', str(link)).group(1)
        # print(url)
        # print(dish.getText())
        # print("------")
        # print("here's the dishies...:")
        for item in result_scrape(url):
          dishes.append(item)

    # for dish in dishes:
    #   print(dish)

    tokens = token_counter(dishes)

    common_tokens_to_exclude = ["food", "foods", "most", "popular", "con", "de", "del", "with", "you", "for", "seafood", "must", "try", "a", "to", "and", "-", "slow", "love", "dishes", "flavorful", "even", "better", "fun", "add", "in", "easy", "amazing", "that", "the"]

    top_dishes = {}

    for k,v in tokens.items():
      key_string = f"{k}"
      if key_string[0].isdigit():
        continue
      elif key_string in common_tokens_to_exclude:
        continue
      elif "(" in key_string:
        continue
      elif ")" in key_string:
        continue
      else:
        # print (f"{k} - {v}")
        top_dishes[key_string] = int(f"{v}")

    # sort by top items desc
    sort_list = sorted(top_dishes.items(), key=lambda x: x[1], reverse=True)

    # print(sort_list)

    top_hit_tokens_list = []

    i = 0
    c = 0
    while c < 10:
      res = sort_list[i]
      if res[0] == '–':
        i += 1
        continue
      elif res[0] == '—':
        i += 1
        continue
      else:
        top_hit_tokens_list.append(res[0])
        c += 1
        i += 1

    # print(dishes)
    # print(top_hit_tokens_list)

    traditional_top_dish_list = {}

    for token in top_hit_tokens_list:
      traditional_top_dish_list[token] = []

    for token in top_hit_tokens_list:
      for dish in dishes:
        dish = dish.lower()
        if token in dish:
          traditional_top_dish_list[token].append(dish)
          
    print(nation, ":  ", top_hit_tokens_list)
    return traditional_top_dish_list