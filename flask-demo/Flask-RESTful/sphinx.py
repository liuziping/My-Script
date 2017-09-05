#!/usr/bin/env python
#coding:utf-8
from flask import Flask,request
import ansible.runner
import os,json

app = Flask(__name__)

def script(dhost,filename="test.sh"):
	results = ansible.runner.Runner(
				module_name = 'shell',
				module_args ='sh /usr/local/sbin/%s' % filename,
				pattern =dhost,forks = 5).run()
	return results


@app.route('/copy/',methods=['GET'])
def index():
	filename = request.args.get('filename')
	shost = request.args.get('shost')
	dhost = request.args.get('dhost')
	status=os.system("/usr/bin/rsync -av %s:/tmp/%s /usr/local/sbin/" % (shost,filename))
	if status == 0:
		status=os.system("/usr/bin/rsync -av /usr/local/sbin/%s %s:/usr/local/sbin/" % (filename,dhost))	
		if status == 0:
			return "ok" 
		else:
			return "rsync to remote fail"
	else:
		return "rsync to sa1 fail"

@app.route('/script/',methods=['GET'])
def scripts():
	filename = request.args.get('filename')
	dhost = request.args.get('dhost')
	res = script(dhost,filename)
	return  json.dumps(res)


if __name__=='__main__':
   app.debug=True
   app.run(host='0.0.0.0',port=5001)
