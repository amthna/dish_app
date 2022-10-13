# Import the beautifulsoup 
# and request libraries of python.
import requests
import bs4
import re
  
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
  
# Iterate through the object 
# and print it as a string.
for dish in dish_results:
    link = dish.find_parent("a")

    url = re.search(r'url=(.*?)&amp', str(link)).group(1)
    print(url)
    print(dish.getText())
    print("------")

# print(soup)