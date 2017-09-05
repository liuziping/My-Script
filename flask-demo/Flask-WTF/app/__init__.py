from flask import Flask
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)

import hello
