import unittest
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from ui_auto_structure import page
from ui_auto_structure.base.base_1 import Base


class PageLogin(Base):
    def page_click_login_link(self):
        self.driver.get("https://dev.acucloud.accuenergy.com")

    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    def page_input_password(self, password):
        self.base_input(page.login_password, password)

    def page_click_login_btn(self):
        self.base_find_element(page.submit)

    def page_get_error(self):
        return self.base_get_text(page.login_error)

    def page_get_screenshot(self):
        self.base_get_screenshot()

    # combination login method
    def page_login(self, username, password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
