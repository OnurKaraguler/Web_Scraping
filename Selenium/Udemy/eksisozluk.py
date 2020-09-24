from selenium import webdriver
import time

browser = webdriver.Chrome()

url = "https://eksisozluk.com/geceye-bir-kedi-ismi-birak--6503209?a=popular"
browser.get(url)

time.sleep(3)

elements = browser.find_elements_by_css_selector(".content")

for element in elements:
    print("*******************************")
    print(element.text)

browser.close()