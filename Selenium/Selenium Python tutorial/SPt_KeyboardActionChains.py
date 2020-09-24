from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains as AC
from selenium.webdriver.common.keys import Keys as K

# exec_path = r"C:\Users\USER\Documents\Selenium\chromedriver.exe"
# URL = r"http://inderpsingh.blogspot.com/2014/08/demowebapp_24.html"
# heading_css_locator = "#Blog1 > div.blog-posts.hfeed > div > div > div.post-outer > div.post.hentry > div.post-body.entry-content > div:nth-child(1) > div > form > h3"
# distance_id_locator = "distance"
# speed_id_locator = "speed"
# wait_time_out = 15
# driver = webdriver.Chrome(executable_path=exec_path)
# wait_variable = WDW(driver,wait_time_out)
# driver.get(URL)
# driver.maximize_window()
# a = AC(driver)
# distance_element = wait_variable.until(EC.presence_of_element_located((By.ID,distance_id_locator)))
# speed_element = wait_variable.until(EC.presence_of_element_located((By.ID,speed_id_locator)))
# distance_element.send_keys("123456")
# a.key_down(K.CONTROL).send_keys("a").perform()
# a.key_down(K.CONTROL).send_keys("c").perform()
# a.click_and_hold(speed_element).perform()
# a.key_down(K.CONTROL).send_keys("v").perform()
############################################################
import pyautogui as PA

exec_path = r"C:\Users\USER\Documents\Selenium\chromedriver.exe"
URL = r"http://inderpsingh.blogspot.com/2014/08/demowebapp_24.html"
heading_css_locator = "#Blog1 > div.blog-posts.hfeed > div > div > div.post-outer > div.post.hentry > div.post-body.entry-content > div:nth-child(1) > div > form > h3"
distance_id_locator = "distance"
wait_time_out = 15
driver = webdriver.Chrome(executable_path=exec_path)
wait_variable = WDW(driver,wait_time_out)
driver.get(URL)
driver.maximize_window()
distance_element = wait_variable.until(EC.presence_of_element_located((By.ID,distance_id_locator)))
distance_element.send_keys("")
PA.write("123456.78")
PA.press("backspace",3)     # three times
PA.hotkey("ctrl","a")
PA.hotkey("ctrl","c")
PA.sleep(1)
PA.press("tab")
PA.hotkey("ctrl","v")

