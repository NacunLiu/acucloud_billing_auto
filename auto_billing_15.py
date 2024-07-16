import unittest

# TestCase TestSute TestLoader(module --run) TestRunner(--run) TextTestRunner Fixture(start/end run)
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
    def setUpClass():
        print('setUpClass called...')
    def tearDownClass():
        print('tearDownClass called...')
    def test01(self):
        print('class03-test01 running...')
    def test02(self):
        print('class03-test02 running...')
    def test03(self):
        print('class03-test03 running...')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # invidually add test method in the class
    suite.addTest(Test01('test01'))
    # Add all test method starts with test in the class
    suite.addTest((unittest.makeSuite(Test03)))
    # provide folder and name of module adding all test class and methods in the module
    # unittest.TextTestRunner().run(unittest.TestLoader().discover("test", pattern="test*.py" ))
    unittest.TextTestRunner().run(suite)

