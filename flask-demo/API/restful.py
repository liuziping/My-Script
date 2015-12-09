#!/usr/bin/env python
#coding:utf-8
from flask import Flask,render_template,request
import json
app = Flask(__name__)

@app.route('/',methods=['GET','POST','PUT','DELETE'])
def index():
	if request.method == 'GET':
#		name = request.args.get("name") #curl  "http://192.168.1.251:5001/?name=wd"
		return "User is %s" % name
	elif request.method =='POST':
#		name = request.form.get('name') #curl  "http://192.168.1.251:5001/"  -d 'name=wd'  -X  POST
		data = request.get_json()
		data = json.loads(data)
		name = data['name']
		return "User is %s" % name
	elif request.method =='PUT':
#		name = request.form.get('name') #curl "http://192.168.1.251:5001/"  -d 'name=wd'  -X  PUT
		data = request.get_json()
		name = data['name']
		return "User is %s" % name
	elif request.method == 'DELETE':
#		name = request.form.get('name') #curl  "http://192.168.1.251:5001/"  -d 'name=wd'  -X DELETE
		data = request.get_json()
		name = data['name']
		return "User is %s" % name


@app.route('/<string:username>',methods=['GET','POST','PUT','DELETE'])   
def test(username):
	if request.method == 'GET':        ##curl  "http://192.168.1.251:5001/wd?age=18"
		age = request.args.get('age')
	elif request.method == 'POST':     #curl "http://192.168.1.251:5001/wd"  -d 'age=18'  -X  POST
		age = request.form.get('age')
	elif request.method == 'PUT':     #curl "http://192.168.1.251:5001/wd"  -d 'age=18'  -X  PUT
		age	= request.json.get('age')
	return "User is %s, and age is %s," % (username,age)

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5001)
