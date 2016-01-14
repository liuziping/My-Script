#coding:utf-8
import os
class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you can not guess'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	#@staticmethod
	#def init_app(app): 
	#	pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='mysql://liuziping:123456@192.168.1.251/test'

class ProductionConfig(Config): 
    SQLALCHEMY_DATABASE_URI='mysql://liuziping:123456@192.168.1.251/devops'

config = {    #不同的配置是注册在字典中。将其中一个配置注册为默认配置。
    'dev' : DevelopmentConfig, 
    'pro' : ProductionConfig,
    'default' : DevelopmentConfig
}
