# https://www.youtube.com/watch?v=7ovFudqFB0Q
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def likeTweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_element_by_class_name('css-1dbjc4n.r-1loqt21.r-16y2uox.r-1wbh5a2.r-1udh08x.r-1j3t67a.r-o7ynqc.r-6416eg')
            # links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            print(tweets)

ed = TwitterBot('onurkaraguler@hotmail.com','onildU8688')
ed.login()
ed.likeTweet('webdevelopment')