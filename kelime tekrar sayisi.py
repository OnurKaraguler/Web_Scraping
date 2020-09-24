# https://www.youtube.com/watch?v=II9mlqPmgII
# https://www.youtube.com/watch?v=4noJ2hJuKx4
# https://www.youtube.com/watch?v=5RNdmnz-meg
# https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w

import requests
from bs4 import BeautifulSoup
import operator

def sozlukOlustur(tumKelimeler):
    kelimeSayisi = {}

    for kelime in tumKelimeler:
        if kelime in kelimeSayisi:
            kelimeSayisi[kelime] += 1
        else:
            kelimeSayisi[kelime] = 1
    return kelimeSayisi


def sembolleriTemizle(tumKelimeler):
    sembolsuzKelimeler = []
    semboller = "0123456789!@$%#^*()_+{}\"<>?,./;:'|[]-=''" + chr(775)
    for kelime in tumKelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol,"")

        if (len(kelime) > 0):
            sembolsuzKelimeler.append((kelime))
    return sembolsuzKelimeler


url = "https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w"
r = requests.get(url)
soup = BeautifulSoup(r.content,features="html.parser")

tumKelimeler = []

for kelimeGruplari in soup.find_all('p'):
    # print(kelimeGrupları)
    icerik = kelimeGruplari.text
    kelimeler = icerik.lower().split()
    # print(kelimeler)

    for kelime in kelimeler:
        tumKelimeler.append(kelime)
        # print(kelime)

tumKelimeler = sembolleriTemizle(tumKelimeler)
# for kelime in tumKelimeler:
#     print(kelime)

kelimeSayisi = sozlukOlustur(tumKelimeler)

for anahtar,deger in sorted(kelimeSayisi.items(),key = operator.itemgetter(1)):
    print(anahtar,deger)