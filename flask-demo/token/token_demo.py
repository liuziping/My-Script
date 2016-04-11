#!/usr/bin/env python
#coding:utf-8
from flask import Flask,request
import base64,time,random,json
app = Flask(__name__)


'''
1：token 是什么？
	官方解释：令牌，代表执行某些操作的权利的对象
	个人理解：用户信息的加密串，系统拿到这个加密串来判断用户是谁，能干什么，不能干什么
2：token 怎么生成
    token的生成方式因人而异，大致思路是将自己需要的一些信息，混合时间戳，随机数等加密生成。我自己的
习惯是 (用户名，用户id，角色，时间戳，随机数)
	  生成token
		token = base64.b64encode(name|uid|role|str(random.random())|int(time.time()+7200))
3: token 怎么用,以判断登录是否过期为例
	先解密token，生成一个列表
	    res=base64.b64decode(token) 
	通过时间戳判断token是否失效
	 	 if int(res.split('|'))[4] > int(time.time())
	  		return True 
'''
def create_token(name,uid,role):
	token = base64.b64encode('%s|%s|%s|%s|%s'%(name,uid,role,str(random.random()),int(time.time()+7200)))  
	return token
    
def verify_token(token):
        t = int(time.time())
        key = base64.b64decode(token)
        print key
        x = key.split('|')
        print x
        if len(x)!=5:
            return json.dumps({'code':1,'errmsg':'token参数不足'})
        if t > int(x[4]):	 
            return json.dumps({'code':1,'errmsg':'登录已过期'})
        else:
            return json.dumps({'code':0,'username':x[0],'uid':x[1],'role':x[2]})

@app.route('/login',methods=['GET','POST'])
def login():
	name = request.form.get('name')
	passwd = request.form.get('passwd')
	if name == "wd" and passwd == "123456": #用户密码正确，则生成要给token,实际开发中需要数据库 
		uid = 1                             #模拟登录成功，从数据库中取到了用户的id,role等信息
		role = 1               
		token = create_token(name,uid,role)
		return json.dumps({'code':0,'token':'%s' % token})
	else:
		return json.dumps({'code':1,'errmsg':'token 创建失败'})

		'''
	    成功生成token的结果
		200
		{"token": "d2R8MXwwfDAuNjYwMDQzNTI5NjkxfDE0NDk4Mzc3OTc=", "code": 0}

		'''

@app.route('/',methods=['GET','POST','PUT'])
def index():
        token = request.args.get('token',None)
        if not token:
            return "token not null"
        result = verify_token(token)   #{"username": "wd", "code": 0, "role": "0", "uid": "1"}
        result=json.loads(result)
        if int(result['code']) == 1:
            return  "error: %s" % result['errmsg']
        if int(result["role"]) == 0:
            return "%s is admin, you can do everything" % result['username']
        else:
            return "%s is not admin, request refuse"  % result['username']


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5002,debug=True)
