#!/usr/bin/env python 
import os 

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you can not guess'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI='mysql://liuziping:liuziping_123456@192.168.1.251/test'
	
class ProductionConfig(Config):	
	SQLALCHEMY_DATABASE_URI='mysql://liuziping:liuziping_123456@192.168.1.251/devops'

config = {
	'dev' : DevelopmentConfig,
	'pro' : ProductionConfig,
	'default' : DevelopmentConfig
}
