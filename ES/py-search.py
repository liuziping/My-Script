#coding:utf-8
from datetime import datetime
import requests
import json

# 创建文档(表)
url = 'http://192.168.1.253:9200/baike/test/'
headers = {'content-type': 'application/json'}
data = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
}

r = requests.post(url,headers = headers,json=data)
print r.text

# 搜索内容
search = {
'query': {
'match': {
    'text': 'cool'
    }
  }
}

url = 'http://192.168.1.253:9200/baike/_search'
r = requests.get(url,headers = headers,json=search)
print r.text
