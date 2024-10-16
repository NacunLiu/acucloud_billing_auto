import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


# this is the practice of the three layer base-po-script model
class Base:
    def __init__(self):
        self.driver = selenium.webdriver.Chrome('../../chromedriver-win64/chromedriver.exe')
        self.driver.maximize_window()

    def base_find_element(self, loc, time=30, frequence=0.5):
        wait = WebDriverWait(self.driver, timeout=time, poll_frequency=frequence)
        element = wait.until(lambda x: x.find_element(*loc))
        return element
    def base_click(self, loc):
        self.base_find_element(loc).click()

    def base_input(self, loc, value):
        element = self.base_find_element(loc)
        element.clear()
        element.send_keys(value)

    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    def base_get_screenshot(self):
        self.driver.get_screenshot_as_file(f'../report/{time.strftime("%Y %m %d %H_%M_%S")}.png')
