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


# 本章内容：类属性与对象属性， 页面对象PO
# 类属性是全体对象所共有的，相当于一个游戏里的最高分，属于这个类而不是任何一个人，类属性必须在类的内部所有函数的外部显示的声明，可以通过cls/self.属性名的方法调用和修改
# 类属性通常应用于所有实例中共享的数据，比如我们的session
# 对象属性相比于类属性更加灵活，通常在__init__方法或者setUp方法中声明，也可以直接在任意一个普通函数内通过self.属性名的方式就声明一个对象属性
# 对象属性可以在后续的任意一个函数中通过self.属性名的方式直接调用和修改
# 对象属性灵活，可以在根据实例的具体情况进行修改，下面的方法就是在setUp方法中声明了self.driver对象属性，并且在后续的测试方法中直接使用
# 在实际测试中将断言放在try里面，捕获异常并且截图，之后继续执行后面的测试用例，防止异常之后直接终断测试
# unittest 只有在整体运行整个测试类的时候才会执行前置和后置方法，单独创建一个对象然后执行某一个方法是不会执行前置和后置方法的

class TestCloud(unittest.TestCase):
    def setUp(self):
        try:
            self.driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
        except Exception as e:
            print(f"Error encountered with ChromeDriverManager: {e}")
            try:
                service = Service('./chromedriver-win64/chromedriver.exe')
                options = Options()
                self.driver = selenium.webdriver.Chrome(service=service, options=options)
            except Exception as e:
                print(f"Error encountered with local ChromeDriver: {e}")
                raise e  # Re-raise the exception if both methods fail
        self.driver.get('https://dev.acucloud.accuenergy.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # def tearDown(self):
    #     self.driver.quit()

    def test01_success(self):
        wait = WebDriverWait(self.driver)

        user = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
        pass_word = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        check_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']")))
        submit = wait.until(EC.presence_of_element_located(By.CSS_SELECTOR, "button[type='submit']"))
        user.clear()
        pass_word.clear()
        user.send_keys('nacun.liu@accuenergy.com')
        password.send_keys('Toz13547')
        submit.click()

    def test02_fail(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        user = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
        pass_word = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        check_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']")))
        submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        user.send_keys('naiu@accuenergy.com')
        pass_word.send_keys('Toz13547')
        submit.click()
        time.sleep(3)
        sign_in_fail = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'si-failure')))
        # print(sign_in_fail.text)
        assert 'failed' in sign_in_fail.text
        time.sleep(3)


class PageLogin():


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    suite.addTest(TestCloud('test02_fail'))
    runner.run(suite)
