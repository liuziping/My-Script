#!/usr/bin/env python
#coding:utf-8
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/task/',methods=['GET','POST','PUT'])
def task_list():
	#name = request.args.get("name")	
	#host = request.args.get("host")	
	name = request.form.get("name")	
	host = request.form.get("host")	
	return "User is %s,host is %s" % (name,host)



if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5002)
