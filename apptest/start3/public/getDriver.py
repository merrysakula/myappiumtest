#coding=utf-8
import time
from start3.public.getdevice import devices
from start3.public.readconfig import config
from start3.public.startappium import appium
from start3.public.logger import logger
from appium import webdriver
from selenium.common.exceptions import WebDriverException
log = logger()
class driver:
    def __init__(self):
        self.config = config()
        self.cmd = devices()
        self.platformVersion = self.cmd.getversion()
        self.deviceName = self.cmd.getdevicename()
        self.platformName = self.config.get_devicevalue('platformName')
        self.appPackage = self.config.get_devicevalue('appPackage')
        self.appActivity = self.config.get_devicevalue('appActivity')
        self.appium = appium(self.deviceName)
        self.appiumport = self.appium.start_appium()
    def mydriver(self):
        desired_caps = {
            'platformName':self.platformName,
            'deviceName':self.deviceName,
            'platformVersion':self.platformVersion,
            'appPackage':self.appPackage,
            'appActivity':self.appActivity,
            'unicodeKeyboard':True,
            'resetKeyboard':True,
            'noReset':True,
            'automationName':'Uiautomator2',
            'newCommandTimeout':180
            }
        try:
            driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.appiumport,desired_caps)
            time.sleep(3)
            log.info('driver success')
            return driver
        except WebDriverException:
            log.warn('driver fail')
if __name__ == '__main__':
    getdriver = driver()
    getdriver.mydriver()