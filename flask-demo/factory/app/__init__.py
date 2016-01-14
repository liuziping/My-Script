#/usr/bin/env python
#coding:utf-8

from flask import Flask,render_template
from flask.ext.sqlalchemy import SQLAlchemy
from config import *

db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	
	#config[config_name].init_app(app)    #和config中的init_app对应，初始化配置文件，目前还不理解
	db.init_app(app)                     #初始化数据库

	#注册蓝图
	from main import main as main_blueprint   
	app.register_blueprint(main_blueprint,url_prefix='/main')

	return app
	

