from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains as AC
import time

exec_path = r"C:\Users\USER\Documents\Selenium\chromedriver.exe"
URL1 = r"http://inderpsingh.blogspot.com/2014/08/demowebapp_24.html"
URL2 = r"https://crossbrowsertesting.github.io/drag-and-drop.html"
heading_css_locator = "#Blog1 > div.blog-posts.hfeed > div > div > div.post-outer > div.post.hentry > div.post-body.entry-content > div:nth-child(1) > div > form > h3"
distance_id_locator = "distance"
draggable_id_locator = "draggable"
droppable_id_locator = "droppable"
wait_time_out = 15
driver = webdriver.Chrome(executable_path=exec_path)
wait_variable = WDW(driver,wait_time_out)
#############################################################
# driver.get(URL1)
# driver.maximize_window()
# heading_element = wait_variable.until(EC.presence_of_element_located((By.CSS_SELECTOR, heading_css_locator)))
# distance_element = wait_variable.until(EC.presence_of_element_located((By.ID, distance_id_locator)))
# a = AC(driver)
# a.double_click(heading_element)
# a.move_to_element_with_offset(distance_element,0,0)
# a.click_and_hold(distance_element)
# a.release()
# a.send_keys("1000")
# a.perform()
#############################################################
# driver.get(URL2)
# draggable_element = wait_variable.until(EC.presence_of_element_located((By.ID,draggable_id_locator)))
# droppable_element = wait_variable.until(EC.presence_of_element_located((By.ID, droppable_id_locator)))
# b = AC(driver)
# b.drag_and_drop(draggable_element, droppable_element)
# b.context_click(draggable_element)
# b.perform()
#############################################################
import pyautogui as PA

exec_path = r"C:\Users\USER\Documents\Selenium\chromedriver.exe"
URL = r"http://inderpsingh.blogspot.com/2014/08/demowebapp_24.html"
distance_id_locator = "distance"
speed_id_locator = "speed"
wait_time_out = 15
driver = webdriver.Chrome(executable_path=exec_path)
wait_variable = WDW(driver,wait_time_out)
driver.get(URL)
driver.maximize_window()
distance_element = wait_variable.until(EC.presence_of_element_located((By.ID, distance_id_locator)))
distance_element.send_keys("1000")
speed_element = wait_variable.until(EC.presence_of_element_located((By.ID, speed_id_locator)))
speed_element.send_keys("50")
# time.sleep(5)
# x,y = PA.position()
# print("X is ", str(x), "Y is ", str(y))
PA.moveTo(180,720,2)
PA.leftClick()