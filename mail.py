#!/usr/bin/env python 
#coding:utf-8
import smtplib
from email.mime.text import MIMEText   
from email.header import Header
import traceback

smtp_host="smtp.******.com"
smtp_port=25                         #默认就是端口就是25,可不写
smtp_login='***@****.com'            #登录用户名
smtp_passwd='***********'            #登录用户密码
smtp_from='***@******.com'           #发件人

def sendmail(subject,content,smtp_to):
	msg = MIMEText(content,_subtype='plain',_charset='utf-8')
	msg['Subject'] = subject
	msg['From'] = smtp_from
	msg['To'] = ";".join(smtp_to)   #多个收件人用 ; 隔开
	try:
		smtp = smtplib.SMTP()                                                  
		smtp.connect(smtp_host)                                       
		smtp.login(smtp_login,smtp_passwd)                    
		smtp.sendmail(smtp_from,smtp_to,msg.as_string())
		smtp.quit()
	except Exception,e:
		 print "Send mail error: %s" % traceback.format_exc()

if __name__=='__main__':
	subject = "这是一封测试邮件"
	content = "这是一封测试邮件"
	smtp_to=['**@163.com','***@qq.com']
	sendmail(subject,content,smtp_to)


