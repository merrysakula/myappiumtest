#coding=utf-8
import unittest
from start3.public.getDriver import driver
from start3.page.login import login
from start3.page.search import search
from start3.page.otccart import otccart
from start3.public.startappium import appium

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver().mydriver()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        appium(cls.driver).stop_appium()
    def test_01_login(self):
        text = login(self.driver).oplogin()
        self.assertEqual(text, '登录成功', '登录失败')
    def test_02_search(self):
        current_activity = search(self.driver).opsearch()
        self.assertEqual(current_activity, 'com.kad.productdetail.ui.ProductDetailActivity', 'search to product fail')
    def test_03_otccart(self):
        current_activity = otccart(self.driver).opotccart()()
        self.assertEqual(current_activity, '.comfirmorder.NewComfirmOrderActivity', 'otc to cart to comforder fail')
        
if __name__ == '__main__':
    unittest.main()
    