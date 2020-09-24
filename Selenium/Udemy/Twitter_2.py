from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://twitter.com/login")
time.sleep(1)

username = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[Oyun_1]/label/div/div[2]/div/input')
password = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')

username.send_keys("onurkaraguler@hotmail.com")
password.send_keys("onildU8688")

girisYap = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div/span/span')
girisYap.click()

time.sleep(1)

searchArea = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[Oyun_1]/div/div/div/form/div[Oyun_1]/div/div/div[2]/input')
searchArea.send_keys("german")
searchArea.send_keys(Keys.ENTER)


browser.close()