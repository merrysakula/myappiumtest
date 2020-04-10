#coding=utf-8
import os
from start3.public.readconfig import config
from start3.public.logger import logger
log = logger()
class devices:
    def __init__(self):
        self.con = config()
#         self.get_devices = self.con.get_cmd('viewPhone')
#         self.get_version = self.con.get_cmd('viewAndroid')
    def getdevicename(self):
        values = os.popen(self.con.get_cmd('viewPhone')).readlines()
        dev = values[1].split()[0]
        if len(values)-2 ==1:
            log.info(dev)
            return dev
        else:
            log.warn('no devices')
    def getversion(self):
        values = os.popen(self.con.get_cmd('viewAndroid')).readlines()
        if values != '':
            version = values[0].split('=')[1]
            log.info('手机版本为：'+version)
            return version.strip()
        else:
            log.warn('no version message')