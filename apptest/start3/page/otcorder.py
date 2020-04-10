#coding=utf-8
import os,time
from start3.public.op import op
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
yamlpath = PATH('../testyaml/otc.yaml')
class otccart:
    def __init__(self,driver):
        self.path = yamlpath
        self.driver = driver
        self.op = op(self.path, self.driver)
    def isaddress(self):
        pass
    def opotccart(self):
        self.op.check_operate_type()
        time.sleep(3)
        return self.driver.current_activity