#coding:utf-8
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you can not guess'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class DevelopmentConfig(Config):
        DEBUG  = True
        URI='mysql://liuziping:123456@192.168.1.251/test'

class ProductionConfig(Config):
        URI='mysql://liuziping:123456@192.168.1.251/devops'

config = { 
        'dev' : DevelopmentConfig,
        'pro' : ProductionConfig,
        'default' : DevelopmentConfig
}
