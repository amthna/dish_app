# Import the beautifulsoup 
# and request libraries of python.
import requests
import bs4
import re
from result_scraper import result_scrape
from token_counter import token_counter
  
# not a bot ;)
headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
}

nation="greece"
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

common_tokens_to_exclude = ["with", "must", "try", "a", "to", "and", "-", "slow", "love", "dishes", "flavorful", "even", "better", "fun", "add", "in", "easy", "amazing", "that", "the"]

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
    top_dishes[f"{k}"] = f"{v}"

# sort by top items desc
sorted(top_dishes.items(), key=lambda x: x[1], reverse=True)

print(top_dishes)
