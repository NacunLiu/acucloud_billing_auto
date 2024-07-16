import unittest
import selenium


# popular assert method

# assertTrue assertFalse assertEqual assertIn
class MyTest_1(unittest.TestCase):
    def test01(self):
       self.assertTrue(0)
       print('1')