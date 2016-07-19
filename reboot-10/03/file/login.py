#/usr/bin/env python
#coding:utf-8
import sys
fo = open("user.txt")
'''
# readline 一行行读取，每行的数据类型为字符串。
num = 1
while True:
    line = fo.readline()
    print repr(line)           # 打印原始的数据，eg:'wd:123456\n' 类型为字符串且带了\n这个字符
    print "%s-->%s" %(num,line.rstrip("\n")) # 每输出一行，前面加个行号，line.rstrip("\n")是把\n干掉，
    num +=1
    if len(line) ==0:
        break;
'''
# 读取所有,并将存为字典
dict = {}
content = fo.readlines()           # 将文件结果存为列表
fo.close()
#print content
for user in content:
    name = user.rstrip("\n").split(":")[0]
    dict[name]=user.rstrip("\n").split(":")[1]
print dict


# 判断用户的账号密码，都ok提示登录成功，否则失败
count = 0
while True:
    count +=1
    if count >3:
        print "对不起，你输入错误过多，账号已经锁定，请联系管理员"
        break;
    name = raw_input("请输入姓名:").strip()
    if name not in dict:
        print "用户不存在，请重新输入"
        continue;
    password = raw_input("请输入密码:").strip()
    if  password != dict[name]:
        print "密码输入有误"
        continue;
    else:
        print "恭喜你，登录成功"
        break;
         
 
