#!/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import json
import requests

headers = {'content-type': 'application/json'}
url = "http://127.0.0.1:5001/api"
data = {
	'jsonrpc':'2.0',
#	'method': 'App.index',    #请求后端无参数的method
#	'method': 'App.name',     #请求后端指定参数的method
#	'method': 'App.user',      #请求后端不定参数的method，通过形参获取参数
	'method': 'App.users',     #请求后端不定参数的method,get_json获取参数
	'id':'1',
	'params':{
		'name':'wd',   #无参数的method，此处为空，指定参数的method，只能保留一条参数
		'age':'18'
	}

}

r = requests.post(url, headers=headers,json=data)

print r.status_code
print r.text




