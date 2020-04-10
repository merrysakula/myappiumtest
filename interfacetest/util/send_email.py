#coding:utf-8
import smtplib
from email.mime.text import MIMEText
class SendEmail:
    global send_user
    global email_host
    global password
    email_host = "smtp.163.com"
    send_user = "@163.com"
    password = ""
    
    def send_email(self,user_list,sub,content):#sub主题，content内容
        user = "mytestte"+"<"+send_user+">"
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] =";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()
        
    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        #90% float类型    #%.2f取小数点后两位    #%%取百分号
        pass_result = "%.2f%%" %(pass_num/count_num*100)
        fail_result = "%.2f%%" %(fail_num/count_num*100)
        user_list = ['@163.com']
        sub = "通过"
        content = "共个数为%s个，通过个数%s，失败个数%s，通过率%s，失败率%s" %(count_num,pass_num,fail_num,pass_result,fail_result)
        self.send_email(user_list, sub, content)
        
if __name__ == '__main__':
    sen = SendEmail()
    sen.send_main([1,2], [3,4,5])
