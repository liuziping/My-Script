#coding:utf-8
from __future__ import unicode_literals                                                                                                                      
from flask import Flask, render_template,session,redirect,request
from  . import app  
import requests,json
import util

headers = {'content-type': 'application/json'}
#deshboard页面
@app.route('/')
def index():
    if session.get('author','nologin') == 'nologin':
        return redirect('/login')
    headers['authorization'] = session['author']
    url = "http://%s/api" % app.config['api_host']
    data = {'jsonrpc': '2.0', 'id': 1, 'method': 'user.getinfo'}
    req = requests.post(url, headers=headers, json=data)
    result = json.loads(json.loads(req.content).get('result', '{}'))
    if result['code'] == 0:
        user = result['user']
        session['user'] = result['user']  #用户信息存入session
        session['role'] = user['r_id'] #角色名eg:['sa','php']
        session['perm'] = user['p_id'].keys()  #权限名eg:['git','mysql']
        session['username'] = user['name'] if user['name'] else user['username']
        return render_template('index.html',info=session,user=session['user'])
    else:
        return redirect('/login')

@app.route('/user/<htmlname>')
def user(htmlname):
    if session.get('author','nologin') == 'nologin':
        return redirect('/login')
    user = session['user']
    user['role'] = ','.join(user['r_id'])
    user['perm'] = ','.join(['<a href="%s" style="color:blue">%s</a>' % (x['url'], x['name_cn']) for x in user['p_id'].values()])
    return render_template(htmlname+'.html',info=session,user=user)

@app.route('/project/<htmlname>')
def project(htmlname):
    if session.get('author','nologin') == 'nologin':
        return redirect('/login')
    username = session.get('username')
    return render_template(htmlname+'.html',info=session,user=username)

@app.route('/cmdb/<htmlname>')
def cmdb(htmlname):
    if session.get('author','nologin') == 'nologin':
        return redirect('/login')
    username = session.get('username')
    return render_template(htmlname+'.html',info=session,user=username)

@app.errorhandler(404)    #系统自带的装饰器，遇到404回自动返回制定的404页面
def not_found(e):
    return render_template('404.html')

@app.errorhandler(500)    
def  internal_server_error(e):
    return render_template('500.html')





