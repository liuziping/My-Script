#!/bin/env python
# -*- encoding: utf-8 -*-

import json
import requests

headers = {'content-type': 'application/json'}
data = { "name": "wd"}
url = "http://192.168.1.251:5001/"

#r = requests.post(url, headers=headers,json=json.dumps(data))  ##后端get_json获取后,类型为<type 'unicode'>，需要json.loads()反解后取值
#r = requests.put(url, headers=headers,data=json.dumps(data))  #后端get_json获取后，类型依旧是<type 'dict'>，可直接取值
r = requests.delete(url, headers=headers,json=data)    #后端get_json获取后，类型依旧是<type 'dict'> ，可直接取值
print r.status_code
print r.text



