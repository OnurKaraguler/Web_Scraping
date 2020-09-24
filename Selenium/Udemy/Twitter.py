from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://twitter.com/login")
time.sleep(3)

username = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[Oyun_1]/label/div/div[2]/div/input')
password = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')

username.send_keys("onurkaraguler@hotmail.com")
password.send_keys("onildU8688")

girisYap = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div/span/span')
girisYap.click()

time.sleep(5)


# browser.close()