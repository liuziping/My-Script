#!/usr/bin/env python
#coding:utf-8

from flask import Flask, render_template,request
import json,urllib

app = Flask(__name__)

def Handleformdata(formdata):   #将类似'id=1&name=lzp&pid=2&pid=3'得表单字符串转为字典
    res = {}
    for x in formdata.split('&'):
        if x.find('=') <= 0:
            continue
        k, v = x.split('=', 1)
        if k in res and isinstance(res[k], list):
            res[k].append(v)
        elif k in res:
            res[k] = [res[k], v]
        else:
            res[k] = v 

    for k in res:
        if isinstance(res[k], list):
            res[k] = ','.join(res[k])
    return res 

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':      #接受原生表单通过action='/',method='POST'提交数据
        print request.form        #ImmutableMultiDict([('username', u'\u4f60\u597d')])
        print dict(request.form)  #{'username': [u'\u4f60\u597d']} 
        username = request.form.get('username')
        print repr(username)   #u'\u4f60\u597d'   flask会自动按照Unicode的转码文本
        print username         #你好
        return render_template("index.html",username=username)
    return render_template("index.html")

@app.route('/add',methods=['GET','POST']) #通过ajax直接提交表单的数据，flask统一解码
def add():
    if request.method == 'POST':  #ajax post直接提交表单serialize()数据
        print request.form        #ImmutableMultiDict([('username', u'\u4f60\u597d')])
        print dict(request.form)  #{'username': [u'\u4f60\u597d']} 
        username = request.form.get('username')
        print repr(username)    #u'\u4f60\u597d\u5417'
        print username          #你好吗
        data = {'username':username}
        return json.dumps(data) 
    if request.method == 'GET':  #ajax getJSON提交表单serialize()数据
        username = request.args.get( 'username')
        print repr(username)   #u'\u4f60\u597d\u5417'
        print username         #你好吗
        data = {'username':username}
        return json.dumps(data)  

@app.route('/add1',methods=['GET','POST']) #ajax将表单字符串整体传到后端，统一交给后端转码和数据类型转换
def add1():
        formdata = request.form.get('formdata') #formdata获取到的是表单通过浏览器编码的字符串，python不识别
        print repr(formdata) #u'username=%E4%BD%A0%E5%A5%BD' 1：中文字符串需要解码，2：把表单字符串转为字典
        print formdata       #username=%E4%BD%A0%E5%A5%BD
        formdata=urllib.unquote(formdata).encode('iso8859-1')
        print repr(formdata) #'username=\xe4\xbd\xa0\xe5\xa5\xbd' 转码为python识别的utf-8，
        print formdata       #username=你好
        data=Handleformdata(formdata)
        return json.dumps(data) 

if __name__=='__main__': 
    app.run(host='0.0.0.0',port=8777,debug=True)
