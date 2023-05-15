import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
print(res.text)
