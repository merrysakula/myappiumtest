#coding=utf-8
from start3.public.baseop import baseop
from start3.public.opelemt import opele

class op:
    def __init__(self,path,driver):
        self.path = path
        self.driver = driver
        self.ope = opele(self.path)
        self.baseop = baseop(self.driver)
    def check_operate_type(self):
        for i in range(self.ope.caselen()):
            if self.ope.get_operate_type(i) == 'click':
                if self.ope.get_find_type(i) == 'id':
                    self.baseop.get_id(self.ope.get_element(i)).click()
                elif self.ope.get_find_type(i) == 'xpath':
                    self.baseop.get_xpath(self.ope.get_element(i)).click()
                elif self.ope.get_find_type(i) =='ids':
                    self.baseop.get_ids(self.ope.get_element(i))[self.ope.get_index(i)].click()
            elif self.ope.get_operate_type(i) == 'send_keys':
                if self.ope.get_find_type(i) == 'id':
                    self.baseop.get_id(self.ope.get_element(i)).send_keys(self.ope.get_send_content(i))
                elif self.ope.get_find_type(i) == 'xpath':
                    self.baseop.get_xpath(self.ope.get_element(i)).send_keys(self.ope.get_send_content(i))
                elif self.ope.get_find_type(i) =='ids':
                    self.baseop.get_ids(self.ope.get_element(i))[self.ope.get_index(i)].send_keys(self.ope.get_send_content(i))
            elif self.ope.get_operate_type(i) == 'toast':
                if self.ope.get_find_type(i) == 'xpath':
                    toast = self.baseop.get_xpath(self.ope.get_element(i).format(self.ope.get_info(i)))
                    text = toast.get_attribute('text')
                    return text
        