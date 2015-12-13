#!/usr/bin/env python
#coding:utf-8
import requests,json
'''
	模拟登陆，并生成token
'''
data =  {'name':'wd','passwd':'123456'}
r = requests.post("http://127.0.0.1:5002/login",data=data)
print r.status_code
print r.text
result = json.loads(r.text)
if result['code'] == 0:
	token = result['token']
else:
	print result['errmsg']

'''
    调用生成的token，进行后面的操作认证。api是无状态的的，先生成一个token，然后用这个token进行后面
权限的认证
    web环境中，通过cookie或者session保存状态的，在用户登录成功获取到token后可以把token存放在session
，然后直接从session中获取到token 
'''
token = {"token":token}
r=requests.get("http://127.0.0.1:5002/",params=token)
print r.status_code
print r.text
