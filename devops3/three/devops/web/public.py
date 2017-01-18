#coding:utf-8
from __future__ import unicode_literals
from flask import Flask, render_template,session,redirect,request
from  . import app  
import requests,json 
import utils,urllib

headers = {"Content-Type": "application/json"}
data = {
        "jsonrpc": "2.0",
        "id":1,
}

def get_url():
    return "http://%s/api" % app.config['api_host']


@app.route('/listapi')
def listapi():
    headers['authorization'] = session['author']
    method = request.args.get('method')
    data['method'] = method+".getlist"
    data['params'] = {}
    utils.write_log('web').info(data)
    r = requests.post(get_url(),headers=headers,json=data)
    utils.write_log('web').info(r.text)
    return r.text 

@app.route('/addapi', methods=['GET','POST'])
def addapi():
    headers['authorization'] = session['author']
    formdata1 = request.form
    print formdata1
    print dict(formdata1)
    formdata = dict((k,','.join(v)) for k,v in dict(request.form).items())
    print formdata
    method = formdata['method']
    data['method'] = method+".create"
    formdata.pop('method')
    data['params']=formdata
    utils.write_log('web').info(data)
    r = requests.post(get_url(),headers=headers,json=data)
    return r.text

@app.route('/getapi')
def getapi():
    headers['authorization'] = session['author']
    method = request.args.get('method')
    data['method'] = method+".get"
    uid = request.args.get('id')
    data['params'] = {
        "m_table":request.args.get('m_table',None),
        'field':request.args.get('field',None),
        's_table':request.args.get('s_table',None),
        'where':{'id':int(request.args.get('id'))}
    }
    utils.write_log('web').info(data)
    r = requests.post(get_url(),headers=headers,json=data)
    return r.text


@app.route('/updateapi',methods=['GET','POST'])
def updateapi():
    headers['authorization'] = session['author']
    print request.form
    print dict(request.form)
    formdata = dict((k,','.join(v)) for k,v in dict(request.form).items())
    print formdata
    method = formdata['method']
    data['method'] = method+".update"
    formdata.pop('method')
    data['params'] = {
        "data":formdata,
        "where":{
            "id":int(formdata['id'])
        }
    } 
    print data
    utils.write_log('web').info(data)
    r = requests.post(get_url(), headers=headers, json=data)
    return r.content

@app.route('/deleteapi')
def deleteapi():
    headers['authorization'] = session['author']
    method = request.args.get('method')
    data['method'] = method+".delete"
    data['params'] = {
        "where":{
         "id":int(request.args.get('id'))
         }
    }
    utils.write_log('web').info(data)
    r = requests.post(get_url(),headers=headers,json=data)
    return r.text

@app.route('/apply/<string:method>')
def applyapi(method):
    headers['authorization'] = session['author']
    data['method'] = 'apply.'+method
    data['params'] = {
         "where":{
         "id":int(request.args.get('id'))
          }
    }
    utils.write_log('web').info(data)
    r = requests.post(get_url(),headers=headers,json=data)
    return r.text
