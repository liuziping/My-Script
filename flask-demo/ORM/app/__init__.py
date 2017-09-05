#!/usr/bin/env python

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://liuziping:liuziping_123456@192.168.1.251/test'
app.config.from_object(config['pro'])
db=SQLAlchemy(app)
#print app.config
#print db
import views
