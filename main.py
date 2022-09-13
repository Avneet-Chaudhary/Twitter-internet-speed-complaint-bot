from selenium import webdriver
from selenium.webdriver.common.by import By

import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "path......"
TWITTER_EMAIL = "Your Email"
TWITTER_PASSWORD = "Your pass...."


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        self.driver.find_element_by_xpath("/html/body/div[7]/div[2]/div/div/div[3]/button").click()

        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    # def tweet_at_provider(self):
    #     self.driver.get('https:/twitter.com/login')
    #     print("Opening Twitter.com")
    #     time.sleep(10)
    #     enter_email = self.driver.find_element(By.XPATH,
    #                                            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
    #     enter_email.send_keys(TWITTER_EMAIL)
    #     next_button = self.driver.find_element(By.XPATH,
    #                                            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
    #     next_button.click()
    #     print("You entered your e-mail")
    #     time.sleep(10)
    #     enter_password = self.driver.find_element(By.XPATH,
    #                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    #     enter_password.send_keys(TWITTER_PASSWORD)
    #     print("You entered your password")
    #     login_button = self.driver.find_element(By.XPATH,
    #                                             '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]')
    #     login_button.click()
    #     print("You logged in!")
    #     time.sleep(5)
    #     # Click on tweet
    #     click_tweet = self.driver.find_element(By.XPATH,
    #                                            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
    #     click_tweet.click()
    #     time.sleep(3)
    #     print("Now I will send tweet...")
    #     # Enter your tweet message
    #     enter_tweet = self.driver.find_element(By.XPATH,
    #                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
    #     enter_tweet.send_keys(f'hello dear idk who! my internet speed is {self.down} download/ {self.up} upload'
    #                           f' {PROMISED_DOWN} down/ {PROMISED_UP} up?')
    #     time.sleep(3)
    #     print("Tweet is ready to post")
    #     # Post your tweet
    #     post_tweet = self.driver.find_element(By.XPATH,
    #                                           '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
    #     post_tweet.click()
    #     print("Tweet is sent!!! Good job!!!")
    #     time.sleep(10)
    #     self.driver.quit()
    def tweet_at_provider(self):
        self.driver.get("https:/twitter.com/login")

        time.sleep(5)
        enter_email = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        enter_email.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
        next_button.click()
        print("You entered your e-mail")
        time.sleep(2)
        enter_password = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        enter_password.send_keys(TWITTER_PASSWORD)
        print("You entered your password")
        login_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]')
        login_button.click()
        print("You logged in!")

        # email = self.driver.find_element_by_xpath(
        #     '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]')
        # email.click()
        # email.send_keys(TWITTER_EMAIL)
        # password = self.driver.find_element_by_xpath(
        #     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        # email.send_keys(TWITTER_EMAIL)
        # password.send_keys(TWITTER_PASSWORD)
        # time.sleep(2)
        # password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
# bot.get_internet_speed()
bot.tweet_at_provider()
