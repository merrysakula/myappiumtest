#coding=utf-8
import os 
from start3.public.op import op
from start3.public.readconfig import config
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
# PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
yamlpath = PATH('../testyaml/search.yaml')
class search:
    def __init__(self,driver):
        self.config = config()
        self.path = yamlpath
        self.driver = driver
        self.op = op(self.path, self.driver)
    def opsearch(self):
        self.appPackage = self.config.get_searchpage('appPackage')
        self.appActivity = self.config.get_searchpage('appActivity')
        self.driver.start_activity(self.appPackage,self.appActivity)
        self.op.check_operate_type()
        current_activity = self.driver.current_activity
        return current_activity
        