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
        element = wait.until(lambda x: x.find_element(*loc)) #之所一些成lambda匿名函数的形式的原因是until方法需要传递一个函数作为参数，之后按照wait
        # 设置的timeout和频率去不断调用这个函数，而且until函数能过滤掉被调用函数返回的NoSuchElement Error的异常，捕获异常之后继续调用，如果找到元素那么until
        # 会直接将元素返回，直到timeout结束 throw exception  
        # 不能直接写driver.find_element()因为这是一个语句，python 解释器按照从左到右的顺序解释执行，如果执行到这条语句发现是语句那么就会先执行这个，而还没有执行
        # until 这就会导致如果第一次尝试找元素没有找到报了异常那么就直接抛出异常报错了
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
        
