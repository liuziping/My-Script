#!/usr/bin/env python
#coding:utf-8
from flask import Flask,render_template,request
from flask_jsonrpc import JSONRPC
import json


app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api')

@jsonrpc.method('App.index')
def index():
    return u'Welcome to Flask JSON-RPC'


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5001)
