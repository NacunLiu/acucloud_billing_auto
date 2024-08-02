import pytest


# pytest建立测试类不需要像unittest一样继承unittest.TestCase而是像任何其他普通类一样直接书写即可
# pytest的测试夹具格式与unittest不一样，直接使用@pytest.fixture(autouse=True)表示方法级的前置测试
# pytest中前置方法和后置方法写在一个函数内部使用统一的装饰器@pytest.fixture(autouse=True)
# 在方法的内部通过yield进行分割，yield语句之后的是后置方法类似于tearDown，yield之前的是前置方法类似于setUp，不写默认是前置方法
# @pytest.fixture(scope="class", autouse=True)表示类方法级的测试前置
# 参数化的方法与unittest不同，不再像unittest中的@parameterized.expand()而是使用@pytest.mark.parameterize("a,b",[(0,1), (1,2)])
# 需要传递两个参数，第一个参数是一个字符串，解释即将传递的参数的名称，第二个参数是元组列表，在里面封装测试数据
# pytest的断言方法与unittest也不一样，不再使用self.assertEqual的形式，而是直接使用内置的python assert语句
# assert c == sum, "Addition result is incorrect" 后边的字符串是在抛出异常后可选择的输出信息
# assert "hello" in "hello world"进行类似于assertIn的断言
# assert 内容 进行True和False的断言 assert 0 -> false   assert 1 -> true
# pytest中不仅没有TestCase，也没有unittest中的测试套件TestSuite TestLoader TestRunner，测试加载以及测试运行,pytest中执行测试用例的方法更简单
# 使用pytest.main(模块名)方法执行测试用例比如 pytest.main('test01.py')
# 或者使用pytest.main(["test_module.py::Test01::test01"])来运行模块中的Test01类中的test01方法
# 或者使用pytest.main(["test_module.py::Test01"])来运行模块中的Test01类中的所有测试方法
# 对于 if __name__ == "__main__"的解释，__name__是一个标识当前运行是否处于主模块的变量，比如我在A 模块中运行A那么就是在主模块，__name__的值就是__main__
# 如果我在B里调用A模块，A模块里也有测试运行语句if __name__ == "__main__"，这时当运行到这条语句的时候，__name__这个值就是B模块的名字而不是__main__那么它后续的代码就不会执行
# class Test01():
#
#     def test01(self, a, b, c):
#         sum = a + b
#         assert c == sum, "Addition result is incorrect"
#
#     def test02(self, a, b, c):
#         sub = a - b
#         assert sub == c, "sub result is incorrect"


class Test02():
    @pytest.fixture(scope="class", autouse=True)
    def setup_teardown_class(self):
        print("class method is called, now test started...")

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        print("method is called, now detail testcase is started...")

    @pytest.mark.parametrize("a, b, c", [(1, 1, 1), (2, 2, 4)])
    def test01(self, a, b, c):
        mult = a * b
        assert mult == c, "Mult result is incorrect"

    # def test02(self, a, b, c):
    #     div = a / b
    #     assert div == c, "div result is incorrect"


if __name__ == "__main__":
    pytest.main(["test_01.py::Test02::test01"])
