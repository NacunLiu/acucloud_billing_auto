import unittest
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import Expected_Conditions as EC


# 本章内容：类属性与对象属性
# 类属性是全体对象所共有的，相当于一个游戏里的最高分，属于这个类而不是任何一个人，类属性必须在类的内部所有函数的外部显示的声明，可以通过cls/self.属性名的方法调用和修改
# 类属性通常应用于所有实例中共享的数据，比如我们的session
# 对象属性相比于类属性更加灵活，通常在__init__方法或者setUp方法中声明，也可以直接在任意一个普通函数内通过self.属性名的方式就声明一个对象属性
# 对象属性可以在后续的任意一个函数中通过self.属性名的方式直接调用和修改
# 对象属性灵活，可以在根据实例的具体情况进行修改，下面的方法就是在setUp方法中声明了self.driver对象属性，并且在后续的测试方法中直接使用
class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = selenium.webdriver.Chrome('./chromedriver-win64/chromedriver.exe')
        self.driver.get('https://dev.acucloud.accuenergy.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test01_success(self):
        wait = WebDriverWait(self.driver)
        user = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
        pass_word = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        check_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']")))
        submit = wait.until(EC.presence_of_element_located(By.CSS_SELECTOR, "button[type='submit']"))
        user.send_keys('nacun.liu@accuenergy.com')
        password.send_keys('Toz13547')
        submit.click()

    def tes02_fail(self):
        wait = WebDriverWait(self.driver)
        user = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
        pass_word = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        check_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']")))
        submit = wait.until(EC.presence_of_element_located(By.CSS_SELECTOR, "button[type='submit']"))
        user.send_keys('naiu@accuenergy.com')
        password.send_keys('Toz13547')
        submit.click()


if __name__ == '__main__':
