import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.cumhuriyet.com.tr/')
# print(r.content)        # sayfanın kaynağını komple alır

soup = BeautifulSoup(r.content,features="html.parser")
# print(soup.prettify())      # sayfa kaynağını güzelleştiriyor
linkler = soup.find_all("a")      # HTML bilgisi gerekli, linkler a etiketi ile tanımlanır. a etiketi ile olan tüm etiketleri çek
# print(x)
# for link in linkler:      # daha güzel görmek için
#     print(link)

# for link in linkler:        # gerçek linkleri almak için
#     print(link.get("href"))

# for link in linkler:        # hangi tuşa bastığımda hangi linke gittiğini anlamam için
#     print(link.text)

for link in linkler:        # hangi linke bastığımda nereye gidiyor
    print(link.text, link.get('href'))