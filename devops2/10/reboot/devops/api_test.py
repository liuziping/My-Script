#/usr/bin/env python
#coding:utf-8
import requests,json 
import utils
import sys
headers = {'content-type': 'application/json'}

username = "admin"
password = "123456"
url = "http://127.0.0.1:2000/api/login?username=%s&passwd=%s" % (username,password)
r = requests.get(url, headers=headers)      #请求API验证用户，并获取token
result = json.loads(r.content)
print result
if result['code'] == 0:
    token = result["authorization"]
    res = utils.validate(token,"123456")  #解密token
    res = json.loads(res)         #return : dict(username:*,uid:*,role:*)
    print  json.dumps({'code':0,'result':res})
else:
    print  json.dumps({'code':1,'errmsg':result['errmsg']})
