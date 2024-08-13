import unittest


# 本章内容：unittest框架
# unittest是单元测试，最小的功能单位的测试，可以是一个函数或者一个类，单元测试属于白盒测试的范围
# 使用unittest执行测试用例的原因：可以批量执行测试用例  可以使用丰富的断言方法  可以生成测试报告
# unittest的核心：TestCase(测试用例) TestSuite(测试套件) TestLoader(测试加载) TestRunner(测试执行)/TextTestRunner(文本方式执行测试用例) Fixture(测试夹具)
# 参数化：为了解决相同操作不同数据的问题，避免代码的冗余 根据需求动态获取参数并引用的过程就是参数化
# unittest并不带参数化,我们需要单独的组件parameterized进行参数化,通过@parameterized.expand(元组列表)
# 在实际测试中，测试数据是不允许出现在代码中的，而是单独保存在一个文件中，再通过代码读出来传递给测试脚本


# TestCase TestSuite TestLoader(module --run) TestRunner(--run) TextTestRunner Fixture(start/end run)
class Test01(unittest.TestCase):
    def test01(self):
        print('class01-test01 running...')

    def test02(self):
        print('class01-test02 running...')

    def test03(self):
        print('class01-test03 running...')


class Test02(unittest.TestCase):
    def setUp(self):
        print('test started...')

    def test01(self):
        print('class02-test01 running...')

    def test02(self):
        print('class02-test02 running...')

    def test03(self):
        print('class02-test03 running...')


class Test03(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass called...')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass called...')

    def test01(self):
        print('class03-test01 running...')

    def test02(self):
        print('class03-test02 running...')

    def test03(self):
        print('class03-test03 running...')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # individually add test method in the class
    suite.addTest(Test01('test01'))
    # Add all test method starts with test in the class
    # 在最新的unittest中已经不再使用unittest.makeSuite进行整个测试类的加载
    # 最新的方法是使用 loader = unittest.TestLoader() suite.addTests(loader.loadTestsFromTestCase(TestCase))
    # suite.addTest((unittest.makeSuite(Test03))) 
    # provide folder and name of module adding all test class and methods in the module
    # unittest.TextTestRunner().run(unittest.TestLoader().discover("test", pattern="test*.py" ))
    unittest.TextTestRunner().run(suite)
