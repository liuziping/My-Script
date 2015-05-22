#!/usr/bin/env python

# FIXME: pep8

# Author : liuziping


import os
import sys
import json
import argparse
import urllib2, urllib
import base64

import ansible.runner

RECEIVERS = (
    'liuziping@douban.com',
    'lihan@douban.com',
    'xutao@douban.com',
    'yongping@douban.com',
    'pengchuan@douban.com',
)

PUSH_KEY = 'v1Wm4xLek6wOqNB0C95u3juvdBmsSWMXQjujBeaJcZrJA'  # xutao@douban.com
PUSH_URL = 'https://api.pushbullet.com/v2/pushes'


def cmds(command,hosts,module="shell",n=5):
   runner = ansible.runner.Runner(
      module_name = module,
      module_args = command,
      pattern =hosts,
      forks = n
   )
   result = runner.run()
   return result
def USA(command,hosts,module="shell",n=5):
   runner = ansible.runner.Runner(
      module_name = module,
      module_args = command,
      pattern =hosts,
      forks = n,
      host_list = '/etc/ansible/beorn'
   )
   result = runner.run()
   return result


def send_message(email, title, body):
    data = {
        "email": email,
        "type": 'note',
        "title": title,
        "body": body,
    }
    payload = urllib.urlencode(data)
    req = urllib2.Request(PUSH_URL)
    base64string = base64.encodestring('%s:%s' % (PUSH_KEY, ''))[:-1]
    authheader =  "Basic %s" % base64string
    req.add_header("Authorization", authheader)

    try:
        resp = json.loads(urllib2.urlopen(req, payload).read())
        return resp['receiver_email'] == email
    except:
        return False


def send_pushbullet(title,content):
    for r in RECEIVERS:
        send_message(r, title, content)


if  __name__=='__main__':   
########## monitor for beorn ####################
    data1=USA('df -h /',"beorn")
    mount1 = str(data1["contacted"]['beorn']['stdout']).split(" ")[-1]
    use1 =  str(data1["contacted"]['beorn']['stdout']).split(" ")[-2]
    if int(use1[:-1]) > 85:
        message1 = "the beorn  %s use is %s"%(mount1,use1)
	#print message1  
	send_pushbullet('PROMBLEM alert: beorn',message1)


##########  monitor for qa  ####################
    list = ["df  -h /"]
    for cmd in list:
        data=cmds(cmd,"qa")

        for host in data['contacted'].keys():
            mount = str(data["contacted"][host]['stdout']).split(" ")[-1]
            use =  str(data["contacted"][host]['stdout']).split(" ")[-2]
            if int(use[:-1]) > 95:
                message = "the %s  %s use is %s"%(host,mount,use)
            #    print message
                title = "PROMBLEM alert: qa %s" % host
                send_pushbullet(title,message)
