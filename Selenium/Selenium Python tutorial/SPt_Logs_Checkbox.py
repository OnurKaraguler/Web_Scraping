from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import SPt_CheckboxFunc as CF
import Utilities as U

exec_path = r"C:\Users\USER\Documents\Selenium\chromedriver.exe"
URL = r"http://inderpsingh.blogspot.com/2013/01/HTMLCSSQuiz1.html"
wait_time_out = 15
check_name_locator = "option"
log_file = "C:\\Python_Examples\\Web_Scraping\\Selenium\\Selenium Python tutorial\\logs\\LogCheckBoxQuiz.txt"
pass_message = "Answered correctly - Question Number"
fail_message = "Answered incorrectly - Question Number"
driver = webdriver.Chrome(executable_path=exec_path)
wait = WDW(driver,wait_time_out)
driver.get(URL)
driver.maximize_window()

i = 0
while i<10:
    i += 1
    driver.execute_script("window.scrollBy(0,120)","")      # Ekranı aşağı kaydırıyor
    check_element_1 = wait.until(EC.presence_of_element_located((By.NAME,check_name_locator + str(i) + '1')))
    check_element_2 = wait.until(EC.presence_of_element_located((By.NAME,check_name_locator + str(i) + '2')))
    check_element_3 = wait.until(EC.presence_of_element_located((By.NAME,check_name_locator + str(i) + '3')))
    check_element_1.click()
    check_element_2.click()
    check_element_3.click() # checkboxes 1, 2 & 3 are selected
    if CF.answered(driver,i):
        U.log("INFO",pass_message +str(i),log_file)
        continue
    check_element_1.click() # checkboxes 2 & 3 are selected
    if CF.answered(driver,i):
        U.log("INFO",pass_message +str(i),log_file)
        continue
    check_element_1.click()
    check_element_2.click()# checkboxes 1 & 3 are selected
    if CF.answered(driver,i):
        U.log("INFO",pass_message +str(i),log_file)
        continue
    check_element_2.click()
    check_element_3.click()# checkboxes 1 & 2 are selected
    if CF.answered(driver,i):
        U.log("INFO",pass_message +str(i),log_file)
        continue
    check_element_2.click()# only 1 is selected
    if CF.answered(driver,i):
        U.log("INFO",pass_message +str(i),log_file)
        continue
    check_element_1.click()
    check_element_2.click()# only 2 is selected
    if CF.answered(driver,i):
        U.log("INFO",pass_message +str(i),log_file)
        continue
    check_element_2.click()
    check_element_3.click()# only 3 is selected
    if CF.answered(driver,i):
        U.log("INFO",pass_message +str(i),log_file)
        continue
    U.log("ERROR",fail_message +str(i),log_file)

