#coding=utf-8
from idna.core import unicode
class CommonUtil:
    def is_contain(self,str_one,str_two):
        '''
                       判断一个字符串是否在另一个字符串中
        str_one:查找字符串
        srt_two:被查找字符串
        '''
        flag = None
        if isinstance(str_one,unicode):
            str_one = str_one.encode('unicode-escape').decode('utf-8')
          
#             str_one = str_one.encode('unicode-escape').decode('string_escape')

        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag
        