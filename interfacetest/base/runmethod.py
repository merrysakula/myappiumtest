#coding:utf-8
import requests
import json
class RunMethod:
    def post_main(self,url,data,header=None):
#         res = None
#         if header != None:
#             res = requests.post(url=url,data=data,headers=header).json()
#         else:
#             res = requests.post(url=url,data=data).json()
#         return res
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
#             print(res.status_code)
        print(url)
        return res.json()
        
    def get_main(self,url,data=None,header=None):
#         res = None
#         if header != None:
#             res = requests.get(url=url,data=data,headers=header).json()
#         else:
#             res = requests.get(url=url,data=data).json()
#         return res
        #格式后
        res = None
        if header != None:
            res = requests.get(url=url,data=data,headers=header)
        else:
            res = requests.get(url=url, params=data)
#             res = requests.get(url=url,data=data)
        print(url)
#             print(res.status_code)
#         return res.text
        return res.json()
        
    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
#         return res
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
