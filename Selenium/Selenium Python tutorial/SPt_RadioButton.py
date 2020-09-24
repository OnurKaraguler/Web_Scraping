# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait as WDW
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# exec_path = r"C:\Users\USER\Documents\Selenium\chromedriver.exe"
# URL = r"http://inderpsingh.blogspot.com/2013/04/SeleniumWebDriverQuiz4.html"
# wait_time_out = 5
# answer1_radio_id_locator = "13"
# answer1_name_locator = "answer1"
#
# driver = webdriver.Chrome(executable_path=exec_path)
# wait = WDW(driver,wait_time_out)
# driver.get(URL)
# driver.maximize_window()
# radio_element = wait.until(EC.presence_of_element_located((By.ID,answer1_radio_id_locator)))
# radio_element.click()
# answer1_element = wait.until(EC.presence_of_element_located((By.NAME, answer1_name_locator)))
#
# # validation
# if "Correct." in answer1_element.get_attribute("value"):
#     print("Test is passed.")
# else:
#     print("Test is failed.")

######################Radio Buttons###############################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import time

exec_path = r"C:\Users\USER\Documents\Selenium\chromedriver.exe"
URL = r"http://inderpsingh.blogspot.com/2013/04/SeleniumWebDriverQuiz4.html"
wait_time_out = 5
answer_radio_id_locator = ""
answer_name_locator = "answer"
score_id_locator = "score"

driver = webdriver.Chrome(executable_path=exec_path)
wait = WDW(driver,wait_time_out)
driver.get(URL)
driver.maximize_window()

for q in range(1,7):        # sayfada 6 soru var
    for a in range(1,5):
        radio_element = wait.until(EC.presence_of_element_located((By.ID,str(q) + str(a))))
        radio_element.click()
        time.sleep(1)
        answer_element = wait.until(EC.visibility_of_element_located((By.NAME, answer_name_locator + str(q))))
        if "Correct." in answer_element.get_attribute("value"):
            break

# validation
score_element = wait.until(EC.visibility_of_element_located((By.ID,score_id_locator)))
if "6/6" in score_element.text:
    print("Test is passed")
else:
    print("Test is failed")
