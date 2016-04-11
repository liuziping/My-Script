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
    username = session.get('username')
    return render_template('index.html',user=username)

@app.route('/user/<htmlname>')
def user(htmlname):
    if session.get('author','nologin') == 'nologin':
        return redirect('/login')
    util.write_log('web').info("info")
    return render_template(htmlname +'.html')

@app.route('/project/<htmlname>')
def project(htmlname):
    if session.get('author','nologin') == 'nologin':
        return redirect('/login')
    return render_template(htmlname +'.html')

@app.route('/cmdb/<htmlname>')
def cmdb(htmlname):
    if session.get('author','nologin') == 'nologin':
        return redirect('/login')
    return render_template(htmlname +'.html')

@app.errorhandler(404)    #系统自带的装饰器，遇到404回自动返回制定的404页面
def not_found(e):
    return render_template('404.html')

@app.errorhandler(500)    
def  internal_server_error(e):
    return render_template('500.html')





