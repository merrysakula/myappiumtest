#coding=utf-8
import unittest
import os
import HTMLTestRunner

#https://www.cnblogs.com/yoyoketang/p/6680503.html
# python2.7要是报编码问题，就加这三行，python3不用加
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
'''
二、diascover加载测试用例

1.discover方法里面有三个参数：

-case_dir:这个是待执行用例的目录。

-pattern：这个是匹配脚本名称的规则，test*.py意思是匹配test开头的所有脚本。

-top_level_dir：这个是顶层目录的名称，一般默认等于None就行了。

2.discover加载到的用例是一个list集合，需要重新写入到一个list对象testcase里，这样就可以用unittest里面的TextTestRunner这里类的run方法去执行。
'''

# 用例路径
case_path = os.getcwd() #os.path.join(os.getcwd(),'testcase')
# case_path = os.path.dirname(os.path.abspath(__file__))    #定位路径为common
# mydir = os.path.split(os.path.realpath(__file__))[0]
# case_path = os.path.join(mydir,'testcase')
# case_path = 'testcase'
# 报告存放路径
report_path = os.path.join(os.getcwd(),'report')
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py', top_level_dir=None)
    print(discover)
    return discover
if __name__ == '__main__':
    # html报告文件路径
    report_abspath = os.path.join(report_path,'../result.html')
    fp = open(report_abspath,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告,测试结果如下：',description=u'用例执行情况：')
    # 调用add_case函数返回值
    runner.run(all_case())
    fp.close()