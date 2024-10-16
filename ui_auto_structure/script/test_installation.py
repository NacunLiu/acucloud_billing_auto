import unittest
from parameterized import parameterized
from ui_auto_structure.page.page_installation import PageInstallation
import time


class TestInstallation(unittest.TestCase):
    page_installation = None

    @classmethod
    def setUpClass(cls):
        cls.page_installation = PageInstallation()

    @classmethod
    def tearDown(cls):
        cls.page_installation.driver.quit()
