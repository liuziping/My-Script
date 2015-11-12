#!/usr/bin/env python
#coding:utf-8
from flask import Flask,request
import ansible.runner
import os,json

"""
 解决 服务器之间文件拷贝和脚本执行的问题（适用于服务器之间做了严格的权限设置，无法互相拷贝只能走跳板机的场景） 
 curl "http://192.168.1.129:5001/script/?filename=build_thesaurus.sh&dhost=cache1"
 curl "http://192.168.1.129:5001/script/?dhost=cache1"     #filename 设置了缺省值，没有参数传来就用默认值
 curl "http://192.168.1.129:5001/copy/?filename=unigram.txt&dhost=cache1&shost=web1"

"""
app = Flask(__name__)

def script(dhost,filename="build_thesaurus.sh"):
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
	if filename is None:
		return "filename not null"
	elif shost is None:
		return "shost not null"
	elif dhost is None:
		return "dhost not null"
	status=os.system("/usr/bin/rsync -av %s:/tmp/%s /tmp/" % (shost,filename))
	if status == 0:
		status=os.system("/usr/bin/rsync -av /tmp/%s %s:/tmp/" % (filename,dhost))	
		if status == 0:
			return "ok" 
		else:
			return "rsync to remote fail"
	else:
		return "rsync to tiaobanji  fail"

@app.route('/script/',methods=['GET'])
def scripts():
	filename = request.args.get('filename')
	dhost = request.args.get('dhost')
	if dhost is None:
		return "dhost is not null"
	if filename is None:   #filename 为空时参数使用默认值
		res = script(dhost)
	else:
		res = script(dhost,filename)
	return  json.dumps(res,indent=4)


if __name__=='__main__':
   app.debug=True
   app.run(host='192.168.1.251',port=5001)

