# coding=utf-8


# def hello():
#     return {'name':'fish'}
# hello 
# print hello()
# print hello()['name']
# FP

# def cooking():
#     print 'cooking is very nice'
#     return 'eggs'
# def fishing():
#     print 'fishing is good'
#     return 'fish'

# def doSth(xxx):
#     print xxx
#     # print xxx() +' is get'
#     # print 'done'

# doSth(fishing)
# print '-'*30
# doSth(fishing())
# print '-'*30
# doSth(cooking)
# print '-'*30
# doSth(cooking())

# 函数 做饭():
#     发个微博 做饭真幸福
#     做了一份西红柿炒鸡蛋
# 函数 钓鱼():
#     发个微博，钓鱼真好
#     钓上一条鱼

# 函数 处理（给我一个技能xx）：
#     执行xx
#     发个微博，xx返回的东西 is get
#     再发个微博，忙完了 done
# 处理（钓鱼）
# 处理（做饭）






# arr = [('age',19),('age',1),('age',13),('age',10),('age',6)]

# print sorted(arr,key=lambda x:x[1])


# import math
# # '阶乘'
# print math.factorial(5)


# import hello
# # 引入hello.py这个文件
# hello.hello_world()

# print hello.name

# from hello import hello_world
# hello_world()

# from hello import *
# from xxx import *
# hello_world()

# from reboot import add 
# add.hello()

# # 引入flask的启动模块 写死的
from flask import Flask
# 新建flask的app 也是写死的
app = Flask(__name__)
 
# 监听路由 就是url 在域名和端口后面的 
# 当域名和端口后面，只有一个/的时候，这个路由触发
@app.route('/')
# 路由对应的处理函数，触发路由的时候执行
# 处理函数的返回值，显示在浏览器
def index():
 return '<button>hello flasl</button>'


if __name__ =='__main__':
    # 启动app，监听端口9092
    app.run(host='0.0.0.0',port=9092,debug=True)

# name_str = 'xiaoming:123\nxiaohua:456\nwoniu:123'
# # print name_str.split('\n')

# new_arr = []
# for line in name_str.split('\n'):
#     new_arr.append(line.split(':'))
# print [line.split(':') for line in name_str.split('\n')]
# print new_arr

# def hello():
#     print 'hello_world'
#     return 'hehe'
#     print 'xxxx'

# hello()

# import config

# config.hello()


# def store_file(user):
#     name = user['name']
#     password = user['password']
#     info_combination = '%s:%s\n' % (name, password)
#     # print info_combination
#     with open('users.txt', 'a') as f:
#         f.write(info_combination)
#     print 'Sign up finished'
#     start_up()
