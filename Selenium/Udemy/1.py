from selenium import webdriver
import time

windowsPath = "C:\Python_Examples\internetten_ver_cekme\Selenium\chromedriver.exe"

browser = webdriver.Chrome(windowsPath)

browser.get("https://www.haberturk.com/")
print(browser.page_source)
print("Site Başlığı: ", browser.title)
browser.refresh()
browser.get("https://www.haberturk.com/ekonomi")
browser.maximize_window()
time.sleep(2)
browser.set_window_size(800,600)
browser.back()

time.sleep(3)
browser.quit()