#!/usr/bin/python
# conding:utf-8

import json
import requests


headers = {'content-type': 'application/json'}
url = "http://http://139.129.10.243/zabbix/api_jsonrpc.php"
data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "Admin",
            "password": "reboot"
        },
        "id": 97
    }

r = requests.post(url,headers=headers, json=data)
print r.status_code
print r.text
