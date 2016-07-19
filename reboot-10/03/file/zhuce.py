#/bin/env python
#coding:utf-8

f = open('user.txt','a+')
'''
# 单条写入
f.write("wd:1234\n")

# 多条写入
names=["kk:123\n","panda:123\n"]
f.writelines(names)

# 交互写入,用户注册
'''
while True:
    name = raw_input("请输入姓名:").strip()
    password = raw_input("请输入密码:").strip()
    repass = raw_input("请再次输入密码:").strip()
    if len(name)==0:
        print "用户名不能为空，请重新输入"
        continue;
    if len(password)==0 or password !=repass:
        print "密码输入有误"
        continue;
    else:
        print "恭喜你，注册成功"
        break;
f.write("%s:%s\n" % (name,password))

f.close()

