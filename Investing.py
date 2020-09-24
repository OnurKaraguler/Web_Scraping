import requests
from bs4 import BeautifulSoup as BS

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
with requests.Session() as ses:
    url = 'https://tr.investing.com/currencies/usd-try'
    r = ses.get(url,headers=headers)
    # print(r.status_code)
    soup = BS(r.content, 'html.parser')
    # print(soup)
    list = soup.find_all('div', {"class":"overViewBox instrument"})
    # print(list)

    for x in list:
        dollar = x.find("div",{"class":"top bold inlineblock"}).find("span").text
        print(dollar)


