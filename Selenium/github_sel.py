from Web_Scraping.Selenium.userInfo import username,password
from selenium import webdriver
import time

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        username = self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        password = self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]").click()

    def getFolowers(self):
        self.browser.get("https://github.com/OnurKaraguler?tab=followers")
        time.sleep(2)

        items = self.browser.find_elements_by_css_selector(".blankslate.mt")


github = Github(username,password)
github.signIn()