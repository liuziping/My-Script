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
	通过生产的token，进行后面的操作，实际环境中可以直接从session中获取到session
'''
token = {"token":token}
r=requests.get("http://127.0.0.1:5002/",params=token)
print r.status_code
print r.text
