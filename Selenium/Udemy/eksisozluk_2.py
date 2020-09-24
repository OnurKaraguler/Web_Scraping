from selenium import webdriver
import random
import time

browser = webdriver.Chrome()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712"

pageCount = 1
entries = []
entryCount = 1
while pageCount <= 10:
    randomPage = random.randint(1,1290)
    newUrl = url + str(randomPage)
    browser.get(newUrl)

    elements = browser.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(3)
    pageCount += 1

for entry in entries:
    print(str(entryCount) + "********************************")
    print(element.text)
    entryCount += 1

browser.close()