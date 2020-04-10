#coding=utf-8
import os

print('os.path.abspath(__file__)>>>',os.path.abspath(__file__))
print('os.path.basename(__file__)>>>',os.path.basename(__file__))
print('os.path.dirname(__file__)>>>',os.path.dirname(__file__))
# mypath =os.path.join(os.getcwd(),'test')
mypath =os.path.abspath(os.path.join(os.path.dirname(__file__))) #lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
print('os.path.join()>>>',mypath)