#!/usr/bin/env python
#coding:utf-8
from . import db

class User(db.Model):
	__tablename__ = 'user' 	
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(60),index=True,unique=True)
	email = db.Column(db.String(60),index=True,unique=True)


	def __repr__(self):
			return '<user %r>' % self.name   #默认输出的字段
