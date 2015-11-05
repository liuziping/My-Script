#!/usr/bin/env python
#coding:utf-8
from flask import Flask,request
import base64,time,random
app = Flask(__name__)

users = {'liuziping':['123456']}

'''
由于字符串中加了时间戳，时间一直在走，故一旦生成字符串就是唯一的
base64.b64encode(':'.join([str("liuziping"),str(random.random()),str(time.time()+7200)]))
'bGl1emlwaW5nOjAuMDM1NDYwOTk0MzQ1NzoxNDQ2NTY3MTIxLjg3'   
解密字符串
token=base64.b64decode('bGl1emlwaW5nOjAuMDM1NDYwOTk0MzQ1NzoxNDQ2NTY3MTIxLjg3')
token解密成字符串后，在通过split转换为列表，最后一个元素是时间戳
token.split(":")
['liuziping', '0.0354609943457', '1446567121.87']
创建字符串时时间戳加了7200s,故7200s之内之前生成的时间戳大于当前时间戳，7200s也就是有效时间了
token.split(":")[-1] >= time.time()
True

In [1]: user = {'liuziping':['111','222']}
In [2]: user['liuziping']
Out[2]: ['111', '222']
In [3]: user['liuziping'].append('3333')
In [4]: user['liuziping']
Out[4]: ['111', '222', '3333']
'''
def create_token(name):
	token=base64.b64encode(':'.join([str(name),str(random.random()),str(time.time()+7200)]))
	users[name].append(token)    
	return token
    
def verify_token(token):
    _token = base64.b64decode(token)
    #token生成列表第一个元素说用户名，用户名作为key,取到user字典中对应存入的token
    if not users.get(_token.split(":")[0])[-1]==token: 
        return -1
    if float(_token.split(":")[-1]) >=time.time():
        return 1
    else:
        return 0

@app.route('/',methods=['GET','POST'])
def index():
    '''
    用户通过账号密码发起request请求时，账号密码会被加密保存到Authorization 中
    request.headers 能打印出请求头信息
    Authorization: Basic bGl1emlwaW5nOjEyMzQ1Ng==
    Content-Length: 
    User-Agent: python-requests/2.8.1
    Connection: keep-alive
    Host: 127.0.0.1:5000
    Accept: */*
    Content-Type: 
    Accept-Encoding: gzip, deflate
    Authorization中的加密串解密后就是我们输入的账号密码了
    In [5]: base64.b64decode('bGl1emlwaW5nOjEyMzQ1Ng==')
    Out[5]: 'liuziping:123456'
    '''
    print  request.headers
    return "hello"


@app.route('/login',methods=['GET','POST'])
def login():
    name,pw = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).split(':')
    if users.get(name)[0] == pw:     #输入的密码正确，则生成要给token 
        return create_token(name)
    else:
        return "error"

@app.route('/test',methods=['GET','POST','PUT'])
def test():
    token = request.args.get('token') 
    if verify_token(token)==1:
        return "ok"
    else:
        return "timeout"


if __name__ == '__main__':
    app.run(debug=True)
