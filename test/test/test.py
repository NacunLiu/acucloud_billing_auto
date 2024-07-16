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
    def test01(self):
        print('class02-test01 running...')
    def test02(self):
        print('class02-test02 running...')
        def test03(self):
         print('class02-test03 running...')
