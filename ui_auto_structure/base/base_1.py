import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# 将页面对象层中所有公共的方法抽取出来放在基类中供本项目或其他项目使用，这样可以减少代码的冗余，同时形成了三层结构
# 三层结构就是 base-PO-业务层(脚本层)
# base称为所有层的基础，基类，放page页面的一些公共的方法，主要给page层用(基本不给脚本层用)
# page层，一个页面封装成一个对象，调用base里的方法，有两种方法调用：1.导包实例化 2.继承 继承更方便
# script层, 也叫业务逻辑(business logical)层，因为真正的业务操作都是在脚本层实现的比如输入用户名，密码，点击登录等等


class Base:
    # 初始化
    def __init__(self):
        self.driver = selenium.webdriver.Chrome('../../chromedriver-win64/chromedriver.exe')
        self.driver.maximize_window()
        # 找元素中自动使用了显示等待，不再需要使用隐式等待
        # self.driver.implicitly_wait(10)
        pass

    # 封装查找元素方法给其他方法使用
    # 使用默认参数法，灵活传递参数(default arguments)
    # *loc表示解包操作，loc=(By.CSS_SELECTOR, ".login") 使用*loc = By.CSS_SELECTOR, ".login"
    # 解包操作*针对的是tuple，list之类的集合，会分解成多个独立的元素但是不会改变单个元素本身的属性是string,Number保持不变
    # 如果不解包直接传入则得到的结果是带引号的,打印结果是('css selector', '.login')
    # 对于在python中如果直接写tp1 = By.CSS_SELECTOR, input[type='text']，虽然看起来语法不对但是会自动组合成一个tuple
    # 使用*loc解包之后的打印结果是css selector .login
    # 传递查找方法和元素标记以及等待时间和频率
    # 在Base中的方法命名以base开头
    # base中存放的都是通用方法，减少代码冗余，提高重复利用率，不放对页面进行具体操作的方法

    def base_find_element(self, loc, timeout=30, poll=0.5):
        # lambda是python中匿名函数的关键字，用来定义一个简单函数，通常只使用一次的函数
        # x是传递给这个匿名函数的参数，就是self.driver
        # ebDriverWait(driver, timeout, poll_frequency)会创建一个等待对象我们称呼他为wait，这个对象操作的对象是driver，
        # 如果使用wait.unitl()方法就会以poll_frequency为频率，以timeout为timeout去不停的让wait去操作driver对象，
        # .until()就是调用wait对象的until方法，每次都是在尝试，然后不断的把driver对象传递进去
        # 直到until里的条件为true，
        # 比如driver.find_element()找到了对象就为ture了结束操作或者找不到不断尝试，直到超时
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_click(self, loc):
        self.base_find_element(loc).click()

    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)
        pass

    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    def base_get_screenshot(self):
        self.driver.get_screenshot_as_file(f'../report/{time.strftime("%Y %m %d %H_%M_%S")}.png')

    loc = (By.CSS_SELECTOR, ".login")
    print(*loc)
