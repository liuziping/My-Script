#!/usr/bin/env python
#coding:utf-8
from flask import Flask, request
from . import app
import  logging, util
import json,time,string,traceback,hashlib

#用户登录验证，并生成token
@app.route('/api/login', methods=['GET'])
def login():
        return "just a test"



