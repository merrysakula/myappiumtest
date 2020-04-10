#coding:utf-8
from util.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse
import json

class DenpendentData:
    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()
    
    #通过case_id获取该case的整行数据
    def get_case_line_data(self,case_id):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data
    
    #执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = run_method.run_main(method, url, request_data,params=request_data)
        return json.loads(res)
    
    #根据依赖的key去获取执行依赖测试case的响应数据，然后返回
    def get_data_for_key(self,row):
        depend_data = self.data.get_depen_key(row)
        response_data =self.run_dependent()
        print(type(depend_data))
        print(type(response_data))
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
#         for i(字典类型) in madle:
#             i.value
        return [math.value for math in madle][0]
    
    
