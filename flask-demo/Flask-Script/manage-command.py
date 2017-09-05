from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@manager.command
def hello(name):
	"just say hello"
	print "hello %s" % name 


if __name__=="__main__":
	manager.run()
