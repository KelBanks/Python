#import libraries

import requests
from bs4 import BeautifulSoup

#Get content from News Website
url = 'https://www.bbc.com/news'
response = requests.get(url)



news = BeautifulSoup(response.text, 'html.parser')
headlines = news.find('body').find_all('h3')
for n in headlines:
    print(n.text.strip())
