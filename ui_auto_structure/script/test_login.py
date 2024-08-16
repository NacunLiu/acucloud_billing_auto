import unittest

from parameterized import parameterized

from ui_auto_structure.page.page_login import PageLogin


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.page_login = PageLogin()

    def tearDown(self):
        self.page_login.driver.quit()

    @parameterized.expand((['nacun.liu@accuenergy.com', '123456']))
    def test_login(self, username, password):
        self.page_login.page_login(username, password)
