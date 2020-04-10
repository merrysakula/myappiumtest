#coding=utf-8
import unittest,requests

class TestA(unittest.TestCase):
    def setUp(self):
        self.g = globals()
    def test_a(self):
        result_a = ' 11 '
        #返回值先给globals()，存到字典对应key
        self.g['a'] = result_a
        self.assertEqual(result_a, ' 11 ')
    def test_b(self):
        b = self.g['a']
        print(b)
        result_b = b+'22'
        self.g['b'] = result_b
        self.assertEqual(result_b, ' 11 22')
    def test_c(self):
        pass
if __name__ == '__main__':
    unittest.main()