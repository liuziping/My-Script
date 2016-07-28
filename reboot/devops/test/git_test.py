#!/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import json
import requests

url = "http://127.0.0.1:1000/api"
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
        res=login('kk','123456')
        result = json.loads(res)
        if int(result['code']) ==0:
            token=result['token']
            headers = {'content-type': 'application/json','authorization':token}
            print token
        else:
            print  result
            return result
        '''
        #create请求
        data = {
                'jsonrpc':'2.0',
                'method': 'role.create',      
                'id':'1',
                'params':{
                  'name':'mysql',   
                  'name_cn': '数据组',
                  'p_id':'1,3',     
                  'info':'dba'  
                }
            }
        '''
        '''
        #getbyid请求
        data = {
                'jsonrpc':'2.0',
                'method': 'project.get',      
                'id':'1',
                'params':{
   #                 'output':['id','name','name_cn'],
                    'where':{'id':1}
                 }
        }
        '''

        #getlist请求
        data = {
                'jsonrpc':'2.0',
                'method': 'project.getlist',      
                'id':'1',
                'params':{
                   }
        }

        ''' 
        #update请求
        data = {
                'jsonrpc':'2.0',
                'method': 'role.update',      
                'id':'1',
                'params':{
  #                  'data':{'name_cn':'db'},
                    'where':{'id':3}
                }
        }
        '''     
       
        '''
        #delete请求
        data = {
                'jsonrpc':'2.0',
                'method': 'project.delete',      
                'id':'1',
                'params':{
                    'where':{'id':8}
                }
        }
        '''
     

        r = requests.post(url, headers=headers,json=data)

        print r.status_code
        print r.text  


rpc()
