import unittest
import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# 模块名称采用page+业务名的小写方式
# 类名采用Page+业务名
# 在类里边，根据业务需求，对每一步操作单独封装成一个方法,之后有复杂的业务需求可以组合使用
class PageLogin:
    def __init__(self):
        self.driver = selenium.webdriver.Chrome('../../chromedriver-win64/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('https://dev.acucloud.accuenergy.com')

    # 输入用户名
    def page_input_username(self, username):
        self.driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(username)

    #     输入密码
    def page_input_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(password)

    #     点击登录
    def page_click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    #     获取异常信息提示
    def page_get_text(self):
        return self.driver.find_element(By.CLASS_NAME, "si-failure").text

    #     组装登录业务方法， 给业务层调用
    def page_login(self, username, password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login()


#   def page_login(self, username, password):
#     wait = WebDriverWait(self.driver, 10)
#
#     user = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
#     pass_word = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
#     check_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']")))
#     submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
#     user.clear()
#     pass_word.clear()
#     user.send_keys(username)
#     password.send_keys(password)
#     submit.click()

# def test02_fail(self):
#     time.sleep(3)
#     wait = WebDriverWait(self.driver, 10)
#     user = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
#     pass_word = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
#     check_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']")))
#     submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
#     user.send_keys('naiu@accuenergy.com')
#     pass_word.send_keys('Toz13547')
#     submit.click()
#     time.sleep(3)
#     sign_in_fail = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'si-failure')))
#     # print(sign_in_fail.text)
#     assert 'failed' in sign_in_fail.text
#     time.sleep(3)
