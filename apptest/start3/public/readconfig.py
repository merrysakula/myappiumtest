#coding=utf-8
import os
import configparser
mypath = os.path.split(os.path.realpath(__file__))[0]
configpath = os.path.join(mypath,'config.ini')
class config:
    def __init__(self):
        with open(configpath) as f:
            data = f.read()
        self.conf = configparser.ConfigParser()
        self.conf.read(configpath)
    def get_devicevalue(self,name):
        return self.conf.get('device',name)
    def get_cmd(self,name):
        return self.conf.get('cmd',name)
    def get_searchpage(self,name):
        return self.conf.get('searchpage', name)
if __name__ == '__main__':
    c = config()
    print(c.get_devicevalue('platformName'))
    print(c.get_searchpage('appActivity'))
