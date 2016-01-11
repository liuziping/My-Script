#!/usr/bin/env python 
#coding:utf-8

from flask import Flask, request,render_template
import  ansible.runner
import os,json,urllib,sys
import util,logging
app = Flask(__name__)

logger  = util.InitLogger("/tmp/jobs.log",logging.INFO,'jobs')
info  = util.InitLogger("/tmp/info.log",logging.DEBUG,'info')
def ansible_cmd(pattern,module,args,forks):
	result = ansible.runner.Runner(
		 	module_name = module,
			module_args = args,
			pattern = pattern,
			forks = forks).run()
	return  result

@app.route('/')
@app.route('/index')
def index():
	return render_template('home.html') 

@app.route('/cmd',methods=['GET','POST'])
def cmd():
	pattern = request.args.get('pattern','all') 
	module = request.args.get('module','shell')
	args = urllib.unquote(request.args.get('cmd','whoami'))
	forks = request.args.get('forks',5)
	results = ansible_cmd(pattern,module,args,forks)
	logger.info("pattern=%s,module=%s,args=%s" % (pattern,module,args)) 
#   return json.dumps(results,indent=4)
	str = ""
	if results is None:
 		print "NO host found"
		sys.exit(1)
	for (hostname,result)  in results['contacted'].items():
		if not "failed" in result and result['stdout'] != "":
#			print "%s | %s | success >>  \n %s" % (hostname,result['cmd'],result['stdout'])
			str += "%s | %s | success >>  \n %s \n" % (hostname,result['cmd'],result['stdout'])
		else:
		 	str += "%s | %s | FAILED  >>  \n %s \n" % (hostname,result['cmd'],result['stderr'])
	for (hostname,result) in results['dark'].items():
			str += "%s | SSH Error >> \n  %s \ n" % (hostname, result['msg'])
	info.debug(str) 
	return str

@app.route('/joblist')
def list():
	str = ''
	with open('/tmp/jobs.log') as f:
		#str = f.read()    #从头到尾读文件
		for line in reversed(f.readlines()): #倒读
			#print line
			str +=line
	return str
if __name__=='__main__':
	app.debug=True 
	app.run(host='0.0.0.0',port=5999)
