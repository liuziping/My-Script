#coding:utf-8
from __future__ import unicode_literals                                                                                                                      
from flask import Flask, render_template,session,redirect,request
from  . import app  
import requests,json,logging
import util

@app.route('/')
def index():
    util.write_log('web').debug("debug")
    return render_template('index.html')


@app.route('/user/<htmlname>')
def user(htmlname):
    util.write_log('web').info("info")
    return render_template(htmlname +'.html')

@app.route('/project/<htmlname>')
def project(htmlname):
    return render_template(htmlname +'.html')

@app.route('/cmdb/<htmlname>')
def cmdb(htmlname):
    return render_template(htmlname +'.html')








