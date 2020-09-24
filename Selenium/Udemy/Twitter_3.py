from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://twitter.com/login")
time.sleep(2)

username = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[Oyun_1]/label/div/div[2]/div/input')
password = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')

username.send_keys("onurkaraguler@hotmail.com")
password.send_keys("onildU8688")

girisYap = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div/span/span')
girisYap.click()

time.sleep(2)

searchArea = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[Oyun_1]/div/div/div/form/div[Oyun_1]/div/div/div[2]/input')
searchArea.send_keys("german language")
searchArea.send_keys(Keys.ENTER)

time.sleep(10)

elements = browser.find_elements_by_css_selector(".content")
print(elements)

# css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0

# for element in elements:
#     print("*************************************")
#     print(element.text)


# time.sleep(10)


# browser.close()