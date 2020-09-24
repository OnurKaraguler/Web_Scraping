# https://www.youtube.com/watch?v=mcX_dIkBf3U&list=PLc3SzDYhhiGUPPWt_rIVszepL1nMTbDaW
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# exec_path = r"C:\Users\USER\Documents\Selenium\chromedriver.exe"  # r text yapar
# URL = r"https://www.wikipedia.org/"
# english_link_locator = "js-link-box-en"
# search_locator = "searchInput"
# search_text = "Software"
#
# driver = webdriver.Chrome(executable_path=exec_path)
# driver.get(URL)
# driver.maximize_window()
# english_link_element = driver.find_element(By.ID,english_link_locator)
# english_link_element.click()
# input_box_element = driver.find_element(By.ID,search_locator)
# input_box_element.send_keys(search_text)
# input_box_element.submit()
# driver.quit()

######################MultipleLanguages###############################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import time

exec_path = r"C:\Users\USER\Documents\Selenium\chromedriver.exe"  # r text yapar
URL = r"https://www.wikipedia.org/"
languages_locators = ["js-link-box-en","js-link-box-tr","js-link-box-de"]
search_locator = "searchInput"
search_text = "Software"
wait_time = 5

driver = webdriver.Chrome(executable_path=exec_path)
driver.get(URL)
# time.sleep(2)     # element hazır olsa bile 2 saniye bekliyor
# driver.implicitly_wait(5)   # max 5 sec for every element but it is very fast
wait = WDW(driver,wait_time)
driver.maximize_window()

for i in range(len(languages_locators)):
    # language_link = driver.find_element(By.ID,languages_locators[i])
    language_link = wait.until(EC.presence_of_element_located((By.ID,languages_locators[i])))
    language_link.click()
    # input_box_element = driver.find_element(By.ID,search_locator)
    input_box_element = wait.until(EC.presence_of_element_located((By.ID,search_locator)))
    input_box_element.send_keys(search_text)
    input_box_element.submit()
    time.sleep(4)
    driver.back()
    driver.back()
# driver.quit()