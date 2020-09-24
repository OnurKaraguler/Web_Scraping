# https://www.youtube.com/watch?v=00bc9BdUPSw
# https://www.imdb.com/chart/top

import requests
from bs4 import BeautifulSoup

imdburl = "https://www.imdb.com/chart/top"

r = requests.get(imdburl)

soup = BeautifulSoup(r.content,features="html.parser")

gelen_veri = soup.find_all("table", {"class":"chart full-width"})

# print(gelen_veri[0].contents)
# print(len(gelen_veri[0].contents))

filmtablosu = (gelen_veri[0].contents)[len(gelen_veri[0].contents) - 2]     # sadece filmlerin olduğu tablo alındı

filmtablosu = filmtablosu.find_all("tr")        # herbir tr listede bir film

for film in filmtablosu:
    filmBasliklari = film.find_all("td",{"class":"titleColumn"})    # herbir filmin içerisinde td -> class titlecolumn için
    print(filmBasliklari)                                           # artık her bir film başlığı bir elemanlı liste
    filmIsmi = filmBasliklari[0].text
    filmIsmi = filmIsmi.replace("\n","")        # boşluk kaldırmak için
    print(filmIsmi)
    print("************************************")