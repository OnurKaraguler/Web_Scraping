import requests
import json

result = requests.get('https://jsonplaceholder.typicode.com/todos')

# result = result.text        # json bilgilerini alabilmek için
# print(result)           # <Response [200]> başarılı bir sonuç verdi
# print(type(result))     # str bilgi gelir

result = json.loads(result.text)

# print(result)           #
# print(type(result))     # list bilgi gelir
# print(result[0])
# print(result[0]['title'])

# for i in result:        # bütün bilgiler satır satır geldi
#     # print(i)
#     print(i['title'])   # sadece title lar

for i in result:        # filtreleme (userId si 1 olan kayıdın titler ları
    if i['userId'] == 1:
        print(i['title'])