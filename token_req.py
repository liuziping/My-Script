#!/usr/bin/env python
#coding:utf-8
import requests

#r = requests.get("http://127.0.0.1:5000/login",auth=('liuziping','123456'))
#print r.text
token = 'bGl1emlwaW5nOjAuMzM4MzM5MDM5OTY6MTQ0NjU3NDI0OC4zNQ=='
r = requests.get("http://127.0.0.1:5000/test",params={'token':token})
print r.text
