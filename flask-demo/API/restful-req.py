#!/bin/env python
# -*- encoding: utf-8 -*-

import json
import requests

headers = {'content-type': 'application/json'}
data = { "name": "wd"}
url = "http://192.168.1.251:5001/"

#r = requests.post(url, headers=headers,json=json.dumps(data))
#r = requests.put(url, headers=headers,json=json.dumps(data))
r = requests.delete(url, headers=headers,json=json.dumps(data))
print r.status_code
print r.text



