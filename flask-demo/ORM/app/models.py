#!/usr/bin/env python
#coding:utf-8
from . import db

class User(db.Model):
	__tablename__ = 'user' 	
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(60),index=True,unique=True,nullable=False)
	email = db.Column(db.String(60),index=True,unique=True,nullable=True)


	def __repr__(self):
			return '<user %r>' % self.name #返回一个具有可读性的字符串表示模型，可在调试和测试时使用
