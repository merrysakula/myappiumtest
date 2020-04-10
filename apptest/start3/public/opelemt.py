#coding=utf-8
import yaml,os
class opele:
    def __init__(self,path):
        self.path = path
    def yamldata(self):
        try:
            #遍历？
#             allpageelements = {}
#             for fpath,dirname,fnames in os.walk(self.path):
#                 for name in fnames:
#                     yamlpath = os.path.join(fpath,name)
#                     print(yamlpath)
#                     if '.yaml' in str(yamlpath):
#                         with open(yamlpath,'r') as f:
#                             data = yaml.full_load(f)
#                             allpageelements.update(data)
#             return allpageelements
            with open(self.path,'r') as f:
                data = yaml.full_load(f)
            return data
        except Exception:
            print('no yaml file')
    def caselen(self):
        return len(self.yamldata()['locators'])
    def get_info(self,i):
        return self.yamldata()['locators'][i]['info']
    def get_element(self,i):
        return self.yamldata()['locators'][i]['element']
    def get_find_type(self,i):
        return self.yamldata()['locators'][i]['find_type']
    def get_operate_type(self,i):
        return self.yamldata()['locators'][i]['operate_type']
    def get_send_content(self,i):
        if self.get_operate_type(i) == 'send_keys':
            return self.yamldata()['locators'][i]['send_content']
    def get_index(self,i):
        if self.get_find_type(i) == 'ids':
            return self.yamldata()['locators'][i]['index']
    def times(self,i):
        pass
if __name__ == '__main__':
    path = '../page/element/login.yaml'
#     path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'page\element')
    ope = opele(path)
    print(ope.yamldata())
    print(ope.caselen())
    print(ope.get_element(0))
    print(ope.get_find_type(0))
    print(ope.get_operate_type(0))
    print(ope.get_send_content(0))