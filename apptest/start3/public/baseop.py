#coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from start3.public.logger import logger
log = logger()
class baseop:
    def __init__(self,driver):
        self.driver = driver
    def get_id(self,id):
        try:
            element = WebDriverWait(self.driver,15).until(lambda driver:self.driver.find_element_by_id(id), 'no ele')
            return element
        except:
            log.error('no ele'+'%s'%(id))
    def get_ids(self,id):
        elements = WebDriverWait(self.driver,15).until(lambda driver:self.driver.find_elements_by_id(id), 'no eles'+'%s'%(id))
        return elements
    def get_xpath(self,xpath):
        element = WebDriverWait(self.driver,15).until(lambda driver:self.driver.find_element_by_xpath(xpath), 'fail xpath')
        return element
            
        