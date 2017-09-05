#!/usr/bin/env python

class Foo:
	def Bar(self):
		print "Bar"

	def Hello(self,name):
		print 'I am %s'  % name
	
obj=Foo()
obj.Bar()
obj.Hello('cjk')


