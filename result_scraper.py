# Import the beautifulsoup 
# and request libraries of python.
import requests
import bs4
import re
import time

time.sleep(1)

dishes = []

def result_scrape(url):
  headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
  }
  params = {
    'gl': 'us',    # country to search from
    'hl': 'en',    # language
  }

  request_result = requests.get(url, headers=headers, params=params)
  
  # Creating soup from the fetched request
  soup = bs4.BeautifulSoup(request_result.text, "html.parser")

  # soup.find.all( h3 ) to grab 
  # all major headings of our search result,
  dish_guesses_1=soup.find_all( 'h3' )
  dish_guesses_2=soup.find_all( 'h2' )

  for dish in dish_guesses_1:
    dish = dish.getText()
    try:
      if dish[0].isdigit():
        dishes.append(dish)
    except:
      continue

  for dish in dish_guesses_2:
    dish = dish.getText()
    try:
      if dish[0].isdigit():
        dishes.append(dish)
    except:
      continue

  return dishes
