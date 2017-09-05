#!/usr/bin/env python
# encoding=utf-8
import ping
import requests
import json

headers = {"Content-Type": "application/json","charset": "utf-8"} 

def ping_idc():
    result = {}
    addr = ['182.18.40.229','182.18.40.223','182.18.40.253']
    for ip in addr:
        percent = ping.quiet_ping(ip)[0]  
        result[ip] = percent 
    return result    # {'182.18.40.227': 0, '182.18.40.229': 100, '182.18.40.252': 0}

def check_web():
    result = {}
    domains = ['www.miaoshou.com','m.miaoshou.com','www.100xhs.com','m.100xhs.com','sapp.miaoshouapi.com','dapp.miaoshouapi.com']
    for domain in domains:
        url = "http://%s" % domain
        result[domain] = requests.get (url).status_code
    return result
    # {'dapp.miaoshouapi.com': 200, 'www.miaoshou.com': 200, 'm.100xhs.com':200, 'm.miaoshou.com': 200, 'www.100xhs.com': 200, 'sapp.miaoshouapi.com':200}


def gettoken():
    data=  {'corpid':'wx43053cde0306cd1a','corpsecret':'OdUzcPVbt1fUkiXBRrQ0n00DAutfQqYZ63I606VLiIvu-UMUFrDKx9jTMgbHgqpT'}
    tokenurl="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    r=requests.get(tokenurl,params=data)
    token = json.loads(r.content)
    token = token['access_token']
    return token 

def sendmsg(msg):
    text =  { 
       #"touser":"liuziping1989",
       #"toparty":3,
       'totag':1,
       "msgtype": "text",
       "agentid": 2,
       "text": {
           "content": "Warning!!! %s" % msg
       },
       "safe":"0"
    }

    token = gettoken() 
    texturl = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % token 
    r = requests.post(texturl, headers=headers, json=text)
    return r.content

if __name__ == '__main__':
    res = ping_idc().values()   # [0, 100, 0]
    if res[0] != 0  and res[1] !=0 and res[2] !=0:
        sendmsg("IDC Network Wrong")
    for domain,status in check_web().items():
        if status != 200:
            msg = "%s NO ACCESS" %  domain
            sendmsg(msg)


