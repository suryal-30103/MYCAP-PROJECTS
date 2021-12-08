# Web scraper using Beutifulsoup4 and requests
import requests
from bs4 import BeautifulSoup

oyo_url= 'https://www.oyorooms.com/hotels-in-bangalore/'

req = requests.get(oyo_url)
content = req.content

print(content)

soup = BeautifulSoup(content, "html.parser")
