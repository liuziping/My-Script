#!/bin/env python
# -*- encoding: utf-8 -*-

import json
import requests



headers = {"Content-Type": "application/json"}
url = 'http://127.0.0.1:5001/api'
data = {
        "jsonrpc": "2.0",
        "method":"App.index",
        "id":1,
        "params":{}
}

r = requests.post(url, headers=headers, json=json.dumps(data))
print r.status_code
print r.content
