#!/usr/bin/env python
#coding:utf-8
import requests
import json
import time 
headers = {"Content-Type": "application/json","charset": "utf-8"} 

def gettoken():
    data={'corpid':'wx43053cde0306cd1a','corpsecret':'OdUzcPVbt1fUkiXBRrQ0n00DAutfQqYZ63I606VLiIvu-UMUFrDKx9jTMgbHgqpT'}
    tokenurl="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    r=requests.get(tokenurl,params=data)
    # print repr(r.content)          # 返回的是json字符串
    token = json.loads(r.content)
    token = token['access_token']
    return token

def sendmsg(msg):
    text = {
       "touser":"liuziping1989",
       #"toparty":3,
       #'totag':1,
       "msgtype": "text",
       "agentid": 2,
       "text": {
           "content": "Warning!!! %s" % msg
       },
       "safe":"0"
    }

    token = gettoken() 
    texturl = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % token 
    r = requests.post(texturl, headers=headers, data=str(text).replace("'",'"'))
    return r.content

print sendmsg("IDC is wrong")
