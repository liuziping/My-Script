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
    return render_template('index.html')


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








