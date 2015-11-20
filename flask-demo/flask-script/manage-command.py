from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

''' 
 python manage.py 
 python manage.py hello  -h
 python manage.py hello wd
'''

@manager.command
def hello(name):
	"just say hello"
	print "hello %s" % name 


if __name__=="__main__":
	manager.run()
