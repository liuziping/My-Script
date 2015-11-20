from . import app,db
from app.models import User
from flask import request
import json,traceback

@app.route('/')
def index():
	#result = User.query.first()
	result = db.session.query(User).first()
	print type(result)                #<class 'app.models.User'>
	user = {}
	user['name'] = result.name
	user['email'] = result.email
	return json.dumps(user,indent=4) 

@app.route('/list')
def list():
	users = []
#	result = User.query.all()            
#	result = User.query.limit(1).all()
	result = db.session.query(User).limit(1).all()
	print type(result)                # <type 'list'>
	for u in result:
		user = {}
		user['name'] = u.name
		user['email'] = u.email
		users.append(user)
	return json.dumps(users,indent=4) 

@app.route('/select')
def select():
	users = []
#	result = User.query.with_entities(User.name,User.email).all()         
	result = db.session.query(User.name,User.email).all()         
	print type(result)              #<type 'list'>
	for u in result:
		user = {}
		user['name'] = u.name
		user['email'] = u.email
		users.append(user)
	return json.dumps(users,indent=4)

@app.route('/filter')
def filter():
	users = {}
	name = {'name':'lzp'}
#	result = db.session.query(User).filter(User.name=='lzp').first()        
#	result = db.session.query(User).filter_by(name='lzp').first()        
	result = db.session.query(User).filter_by(**name).first()        
	if result is None:        #for first()
		return json.dumps({'code':1,'msg':'user is not exist'})
	users['name'] = u.name
	users['email'] = u.email
	return json.dumps(users,indent=4) 
	

@app.route('/add')
def add():
	try:
		name = request.args.get('name')   # curl "http://ip:port/add?name=lzp&email=lzp@163.com
		email = request.args.get('email')
		#u = User(name=name,email=email)
		data = {}                                  
		data['name']=name
		data['email']=email
		u = User(**data)
		db.session.add(u)
		db.session.commit()
		return json.dumps({'code':0,'msg':'add user %s is sucess' % name})
	except :
		return json.dumps({'code':1,'msg':'add user error: %s' % traceback.format_exc()},indent=4)

@app.route('/update')
def update():
	try:
		email = {"email":'lzp@qq.com'}
		names = {'name':'lzp'} 
		db.session.query(User).filter_by(**names).update(email)
		db.session.commit()
		return json.dumps({'code':0,'msg':'update  user  sucuss' })
	except:
		return json.dumps({'code':1,'msg':'update user error'})

@app.route('/delete')
def delete():
	try:
		name = {'name':'lzp'} 
#		db.session.query(User).filter_by(**name).delete()
		User.query.filter_by(**name).delete()
		db.session.commit()
		return json.dumps({'code':0,'msg':'delete  user  sucuss' })
	except:
		return json.dumps({'code':1,'msg':'delete user error'})
