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


class PageInstallation(Base):
    def page_click_installation(self):
        self.base_click(page.installation_navi)

    def page_click_devices(self):
        self.base_click(page.device_navi)