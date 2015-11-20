#coding:utf-8
from flask_script import Manager,prompt_bool
from app import app,db
from app.models import User

manager = Manager(app)

@manager.command
def create():
	db.create_all()

@manager.command
def drop():
	if prompt_bool("Are you sure you want to drop all your data"):
		db.drop_all()

@manager.command
def save():
	user = User(name='admins',email='admins@ddsds.com')
	db.session.add(user)
	db.session.commit()

@manager.command
def  select():
	users = User.query.all()
	for u in  users:
		print "my name is %s,email is %s" % (u.name,u.email)

if __name__ == '__main__':
	manager.run()
