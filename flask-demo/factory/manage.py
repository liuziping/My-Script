#/usr/bin/env python
#coding:utf-8

from app import create_app,db
#from app.models import *
from flask.ext.script import Manager,Shell
from flask.ext.migrate import Migrate,MigrateCommand

app = create_app('dev')
manager = Manager(app)
migrate = Migrate(app,db)

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5998,debug=True)
