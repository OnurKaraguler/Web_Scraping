from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select        # for dropdown
import time

exec_path = r"C:\Users\USER\Documents\Selenium\chromedriver.exe"
URL = r"http://inderpsingh.blogspot.com/"
wait_time_out = 15
driver = webdriver.Chrome(executable_path=exec_path)
driver.get(URL)
wait_variable = WDW(driver,wait_time_out)
driver.maximize_window()

# links = wait_variable.until(EC.visibility_of_any_elements_located((By.TAG_NAME, "a")))
# print("The total number of links is", len(links))
# for link in links:
#     print(link.text)
wait_variable.until(EC.element_to_be_clickable((By.LINK_TEXT, "Selenium Python Tutorials"))).click()
driver.back()
wait_variable.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Selenium Python"))).click()