html_doc = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk web sayfam</title>
</head>
<body>
    <h1 id="header">
        Python kursu
    </h1>

    <div class="group1">       # Grup oluşturulur, class -> grup ismi
        <h2>
            Programlama
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <div class="group2">
        <h2>
            Modüller
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <div class="group3">
        <h2>
            Django
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="Onur_Karaguler.png" alt="">

<a href="http://example1.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example2.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example3.com/elsie" class="sister" id="link1">Elsie</a>

</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify()
result = soup.title
result = soup.head
result = soup.body
result = soup.title.name
result = soup.title.string      # içerisindeki ifadeyi alır
result = soup.h1
result = soup.h2            # ilk h2 yi getirir
result = soup.h2.name
result = soup.h2.string

result = soup.find_all('h2')
result = soup.find_all('h2')[0]
result = soup.find_all('h2')[1]

result = soup.div
result = soup.find_all('div')[1]
result = soup.find_all('div')[1].ul.find_all('li')

result = soup.div.findChildren()        # tüm alt elemanları ver
result = soup.div.findNextSibling()     # group2 geldi
result = soup.div.findNextSibling().findNextSibling()

# print(result)

result = soup.find_all('a')

for link in result:
    # print(link)
    print(link.get('href'))         #linkleri almak için

