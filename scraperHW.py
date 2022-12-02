from bs4 import BeautifulSoup
import requests

url = "https://www.zomato.com/istanbul/restoranlar"

agent = {"User-Agent":"Mozilla/5.0"}

r = requests.get(url, headers=agent)

soup = BeautifulSoup(r.content, features="lxml")

for name in soup.find_all("h4"):
    print(name.text)

