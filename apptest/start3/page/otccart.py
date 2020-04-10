#coding=utf-8
import os,time
from start3.public.op import op
# from start3.public.readconfig import config
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
# PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
yamlpath = PATH('../testyaml/otc.yaml')
class otccart:
    def __init__(self,driver):
#         self.config = config()
        self.path = yamlpath
        self.driver = driver
        self.op = op(self.path, self.driver)
    def opotccart(self):
#         self.appPackage = self.config.get_searchpage('appPackage')
#         self.appActivity = self.config.get_searchpage('appActivity')
#         self.driver.start_activity(self.appPackage,self.appActivity)
        self.op.check_operate_type()
        time.sleep(3)
        return self.driver.current_activity