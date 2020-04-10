#coding:utf-8
import requests
import json
from xlutils.copy import copy
import xlrd


#get cookie
url = ''
data = {
    "loginName":"",
    "password":"",
    "validateCode":""
    }
res = requests.post(url,data)
cookies = res.cookies
cookie = requests.utils.dict_from_cookiejar(cookies)
print(cookie)
for a in cookies:
    print(a.name,a.value)
#write cookie into excel
# read_data = xlrd.open_workbook('../dataconfig/trycookie.xls')
# write_data = copy(read_data)
# sheet_data = write_data.get_sheet(0)
# sheet_data.write(1,5,a.name)
# write_data.save('../dataconfig/trycookie.xls')
#write cookie into jsonfile
result = {"write":cookie}
readed = json.load(open('cookie.json','r'))
json.dump(readed, open('cookie.json','w'))

with open('cookie.json','w') as fp:
    fp.write(json.dumps(result,indent=4))

# class OperationHeader:
#     def write_cookie(self,row):
        