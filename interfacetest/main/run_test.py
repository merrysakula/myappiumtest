#coding:utf-8
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DenpendentData
from jsonpath_rw import jsonpath,parse
from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperationJson

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mail =SendEmail()
    
    def go_on_run(self):
#         res = None 
#         rows_count = self.data.get_case_lines()
#         print(rows_count)
#         for i in range(1,rows_count):
#             print(i)
#             url = self.data.get_request_url(i)
#             print(url)
#             method = self.data.get_request_method(i)
#             is_run = self.data.get_is_run(i)
#             data = self.data.get_data_for_json(i)
#             expect =self.data.get_expect_data(i)
#             header = self.data.is_header(i)
#             if is_run:
#                 res = self.run_method.run_main(method, url, data, header)
#                 print(res) 
#                 if self.com_util.is_contain(expect, res):
#                     self.data.write_result(i, 'pass')
# #                     print('pass')
#                 else:
#                     self.data.write_result(i, 'fail')
#                     print('fail')
            
#             return res#为什么不能return


        res = None 
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                print(i)
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                expect =self.data.get_expect_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DenpendentData(depend_case)
                    #获取依赖的响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_response_data
                    
                if header == 'write':
                    res = self.run_method.run_main(method, url, request_data)
                    op_header = OperationHeader(res)
                    op_header.write_cookie()
                    
                elif header == 'yes':
                    op_json = OperationJson('../dataconfig/cookie.json')
                    cookie = op_header.get_data('apsid')
                    cookies = {
                            'apsid':cookie
                        }
                    res = self.run_method.run_main(method, url, request_data, cookies)
                else:
                    res = self.run_method.run_main(method, url, request_data)
                      
#                 res = self.run_method.run_main(method, url, request_data, header)
                
                if self.com_util.is_contain(expect, res):
                    self.data.write_result(i, 'pass')
                    pass_count.append(i)
                else:
                    self.data.write_result(i, res)
                    fail_count.append(i)
        print(len(pass_count))
        print(fail_count)
        self.send_mail.send_main(pass_count, fail_count)    
        
if __name__ == '__main__':
    run = RunTest()
    print(run.go_on_run())
    order = {'data': 
             {
                 'url': ['',
                       ''
                       ],
                 'userInfo': {'uid': ''}}, 'msg': '成功', 'status': }
    res = "data.userInfo.uid"
    json_exe = parse(res)
    madle = json_exe.find(order)
    print([math.value for math in madle][0])
    
