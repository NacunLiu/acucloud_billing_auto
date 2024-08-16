import unittest
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from auto_billing_17 import PageLogin


# 本章内容：UI测试的结构和方法封装
# PO page object 页面对象 把整个页面封装到一个class里，每一步单独的操作封装一个方法，比如输入用户名封装一个方法，点击登录按钮封装一个方法，获取文本信息封装一个方法
# 在结构组织上：page(文件夹)--page_实意名(模块名，比如page_login)-模块名改大驼峰(类名)
# 与api测试类似的，所有接口url的组织在api模块中一样，将所有页面操作相关的内容组织在page模块中，然后在测试用例script中调取页面操作

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login = PageLogin()

    def tearDown(self):
        pass

    def test_login(self):
        pass
