# https://www.youtube.com/watch?v=ng2o98k983k
from bs4 import BeautifulSoup
import requests
import csv

r = requests.get('https://coreyms.com/')
soup = BeautifulSoup(r.content,'lxml')
# print(soup.prettify())

csv_file = open('cmc_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'youtube_link'])

###################For first article#######################
# # article = soup.find('article')
# # print(article.prettify())
#
# # article = soup.find('article')
# # headline = article.h2.a.text
# # print(headline)
#
# # article = soup.find('article')
# # summary = article.find('div',class_='entry-content').p.text
# # print(summary)
#
# article = soup.find('article')
# video_source = article.find('iframe', class_='youtube-player')['src']
# # print(video_source)
#
# vid_id = video_source.split('/')[4]
# vid_id = vid_id.split('?')[0]           # Youtube video id bulmak için
# # print(vid_id)
#
# youtube_link = f'https://youtube.com/watch?v={vid_id}'
# print(youtube_link)

###################For all articles#######################
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        video_source = article.find('iframe', class_='youtube-player')['src']

        vid_id = video_source.split('/')[4]
        vid_id = vid_id.split('?')[0]

        youtube_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        youtube_link = None

    print(youtube_link)

    print()

    csv_writer.writerow([headline,summary,youtube_link])

csv_file.close()