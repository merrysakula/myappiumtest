#coding=utf-8
from start3.public.op import op
import os
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
# PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
yamlpath = PATH('../testyaml/login.yaml')
class login:
    def __init__(self,driver):
#         pass
        self.path = yamlpath
        self.driver = driver
        self.op = op(self.path, self.driver)
    def oplogin(self):
        return self.op.check_operate_type()
if __name__ == '__main__':
    pass
#     print(PATH)