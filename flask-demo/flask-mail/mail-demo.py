#!/usr/bin/env python 
#coding:utf-8
import smtplib
from email.mime.text import MIMEText                                 #MIME文本对象
from email.header import Header

subject = '邮件主题'
email_info = "这是一封测试邮件"
maillist = ['787696331@qq.com','liuziping@yuanxin-inc.com']          #收件人
maillist = ';'.join(maillist)

msg = MIMEText(email_info,'plain','utf-8')                           #实例化msg
msg['Subject'] = subject

smtp = smtplib.SMTP()                                                #定义一个smtp实例
smtp.connect('smtp.mxhichina.com:25')                                #连接的服务器msg
smtp.login('online@yuanxin-inc.com','*********')                     #发送方的信息
smtp.sendmail('online@yuanxin-inc.com',maillist,msg.as_string())     #内容以字符串形式发送   
smtp.quit()
