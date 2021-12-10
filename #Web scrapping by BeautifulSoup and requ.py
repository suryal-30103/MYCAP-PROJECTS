#Web scrapping by BeautifulSoup and requests
import requests
from bs4import BeautifulSoup

oyo_url="https://www.oyorooms.com/hotels-in-bangalore/"

req = requests.get(oyo_url)
content=req.content

print(content)

soup = BeautifulSoup(content,"html.parser")

all_hotels = soup.find_all("div", {"class" : "hotelCardListing"})

for hotel in all_hotels:
    hotel_name = hotel.find("h3" , {"class" : "listingHotelDescription__hotelName"}).text
    hotel_address = hotel.find("span" , {"itemprop" : "streetAddress"}).text
    print(hotel_name,hotel_address)



