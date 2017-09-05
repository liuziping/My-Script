from flask import Flask
from flask.ext.script import Command
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

class Hello(Command):
	'prints hello world'

	def run(self):
		print "hello world"

manager.add_command('hello',Hello())
manager.run({'hello':Hello()})

if __name__=="__main__":
	manager.run()
