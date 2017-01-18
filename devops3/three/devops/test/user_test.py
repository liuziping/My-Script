#!/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import json
import requests

url = "http://127.0.0.1:2000/api"
#登录并获取token
def login(username,password):
        rep_url = "%s/login?username=%s&passwd=%s" % (url,username,password)
        r = requests.get(rep_url)      
        result = json.loads(r.content)
        if result['code'] == 0:
            token = result["authorization"]
            return json.dumps({'code':0,'token':token})
        else: 
            return json.dumps({'code':1,'errmsg':result['errmsg']})

def rpc():
        res=login('admin','123456')
        result = json.loads(res)
        if result['code'] ==0:
            token=result['token']
            headers = {'content-type': 'application/json','authorization':token}
            print token
        else:
            return result
        '''
        #create请求
        data = {
                'jsonrpc':'2.0',
                'method': 'user.create',      
                'id':'1',
                'params':{
                    'username':'panda',
                    'password':'123456',
                    'repwd':'123456',
                    'name':'panda',
                    'email':'787696331@qq.com',
                    'mobile':'121212121',
                    'r_id':'1,3',
                    'is_lock':0
                }
            }
        '''
        '''
        #get请求
        data = {
                'jsonrpc':'2.0',
                'method': 'user.get',      
                'id':'1',
                'params':{
                    'output':['id','username','name','email','mobile'],
                    'where':{'id':2}
                }
        }
        '''
        #getlist请求
        data = {
                'jsonrpc':'2.0',
                'method': 'user.getlist',      
                'id':'1',
                'params':{
                    'output':['id','username','name'],
                }
        }
        '''
        #getinfo请求
        data = {
                'jsonrpc':'2.0',
                'method': 'user.getinfo',      
                'id':'1',
                'params':{
                }
        }
        '''
        '''
        #update请求
        data = {
                'jsonrpc':'2.0',
                'method': 'user.update',      
                'id':'1',
                'params':{
                    'data':{'r_id':'1,3'},
                    'where':{'id':'3'}
                }
        }
        '''
        '''
        #delete请求
        data = {
                'jsonrpc':'2.0',
                'method': 'user.delete',      
                'id':'1',
                'params':{
                    'where':{'id':'5'}
                }
        }
        '''
        '''
        #/git/password修改密码 
        data = {
            #'oldpassword':'123456',
            'user_id':1,
            'password':'123456'
        }
        r = requests.post("http://127.0.0.1:2000/api/password", headers=headers,json=data)
        '''
        r = requests.post(url, headers=headers,json=data)

        print r.status_code
        print r.text 


rpc()
