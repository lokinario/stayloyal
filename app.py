from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

class TwitterBot:
    def __init__(self, user, pw):
        self.user = user
        self.pw = pw
        self.bot = webdriver.Firefox() 
    
    def login(self):
        bot = self.bot 
        bot.get('https://twitter.com/login')
        time.sleep(3)
        user = bot.find_element_by_name('session[username_or_email]')
        pw = bot.find_element_by_name('session[password]')
        user.clear()
        pw.clear()
        user.send_keys(self.user)
        pw.send_keys(self.pw)
        pw.send_keys(Keys.RETURN)
        time.sleep(3)
    
    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        for _ in range(10):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
        print(links)
        # for l in links:
        #     bot.get('https://twitter.com'+l)
        #     try:
        #         bot.find_elements_by_class_name('HeartAnimation').click()
        #           data-testid="like"
        #         time.sleep(5)
        #     except Exception as x:
        #         print(x)
        #         time.sleep(60)
test = TwitterBot('robstartest','testtesttest') 
test.login()
test.like_tweet('blm')  

