import requests
from bs4 import BeautifulSoup
url = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar'

html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

# list = soup.find_all('li', {"class":"column"},limit=5)
list = soup.find_all('li', {"class":"column"})

for li in list:
    name = li.div.a.h3.text.strip()         # başında ve sonundaki boşluklar silinir
    link = li.a.get('href')
    oldprice = li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip('TL')
    newprice = li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip('TL')

    # print(oldprice, newprice)

    print(f"name: {name} link: {link} old price: {oldprice} new price: {newprice}")