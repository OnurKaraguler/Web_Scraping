import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
# print(html)

# list = soup.find('tbody', {"class":"lister-list"}).find_all("tr",limit=1)       # limit=1 sadece 1 tanesi
list = soup.find('tbody', {"class":"lister-list"}).find_all("tr",limit=50)       # limit=1 sadece 1 tanesi

count = 0
for tr in list:
    title = tr.find("td", {'class':'titleColumn'}).find('a').text
    year = tr.find("td", {'class':'titleColumn'}).find('span').text.strip("()")  # silinmesi gereen karakterler
    rating = tr.find("td", {'class':'ratingColumn imdbRating'}).find('strong').text
    count += 1
    # print(title, year)
    print(f"{count}- film: {title.ljust(50)} yıl: {year} değerlendirme: {rating}")      #ljust(50) 50 karakter içerisinde sola

# print(list)
# content = response.content
# print(content)