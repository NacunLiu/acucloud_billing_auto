import unittest

from parameterized import parameterized

from ui_auto_structure.page.page_login_update import PageLogin
import time


# 使用方法级别或者类级别的前置方法进行初始化设置都可以，没有很大区别
# 如果使用方法级别前置方法进行page的对象实例化，那么对于每一组参数，都会从新实例化一个页面对象，而测试结束也会关闭浏览器
# 如果使用类级别前置方法进行page的对象初始化，那么只会在测试开始时打开浏览器一次并在结束所有测试数据后关闭浏览器
# 类属性必须在方法外显示的定义
# 改变类属性有两种方法： 1.在类的外部，直接通过 类名.类属性名 = new_value的方法改变
# 2. 在类的内部通过类方法cls.类属性 = new_value的方法改变
# 典型的错误是通过 对象名.类属性 = new_value或者 在类的内部通过方法级别 self.类属性 = new_value实质上都是在对这个单一的对象
# 创建了一个新的对象级别方法,并没有改变类属性或者其他对象的类属性 但是对于这个单个对象,因为它的新定义的对象属性和类属性同名
# 所以该对象的class attribute is override.
# 简单来说当我们使用一个attribute的时候,python会先在对象的属性中查找,如果找到就直接使用,类属性就会被ignore,如果找不到对象属性,那么才回去
# 类属性中继续查找,直到找到为止
class TestLogin(unittest.TestCase):
    # 可以使用方法级别的setUp和tearDown也可以使用类级别的setUpClass和tearDownClass
    # def setUp(self):
    #     # 获取登录页面对象，实例化之后测试方法中调用
    #     self.page_login = PageLogin()
    #     self.page_login.page_click_login_link()
    #
    # def tearDown(self):
    #     # 关闭浏览器，使用login下面的driver
    #     self.page_login.driver.quit()
    page_login = None

    @classmethod
    def setUpClass(cls):
        cls.page_login = PageLogin()
        cls.page_login.page_click_login_link()

    @classmethod
    def tearDownClass(cls):
        cls.page_login.driver.quit()

    @parameterized.expand((['nacun.liu@accuenergy.com', '123456'], ['nacun.liu@accuenergy.com', 'Toz13547']))
    def test_login(self, username, password):
        self.page_login.page_click_login_link()
        time.sleep(3)
        self.page_login.page_login(username, password)
        time.sleep(3)
        msg = self.page_login.page_get_error()
        try:
            # 断言
            self.assertEqual(msg, "sign in failed")
            print(msg)
        except Exception as e:
            self.page_login.driver.get_screenshot_as_file(f'../report/{time.strftime("%Y-%m-%d %H_%M_%S")}.PNG')


if __name__ == '__main':
    unittest.main()
