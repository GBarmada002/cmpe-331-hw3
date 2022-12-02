"""
Stage: Development 1
@author: Ghassan Barmada 120202001
@author: Burak Seymen 117202076
from bs4 import BeautifulSoup
import requests

url = "https://www.zomato.com/istanbul/restoranlar"

agent = {"User-Agent":"Mozilla/5.0"}

r = requests.get(url, headers=agent)

soup = BeautifulSoup(r.content, features="lxml")

for name in soup.find_all("h4"):
    print(name.text)

