#!/usr/bin/env  python
#coding:utf-8
'''
http://coolshell.cn/articles/11265.html
http://www.cnblogs.com/SeasonLee/articles/1719444.html 
'''
## 获取装饰器中的参数
## 方法一：约定好参数名装饰器中返回，回调函数直接调用 
def hello(fn):
	def wrapper():
		print "hello, %s" % fn.__name__
		name =  ['lzp','18']
		str = "hello world"
		user = {'email':'lzp@126.com'}
		return fn(name,str,user)
	return wrapper
@hello
def foo(name,str,user):
	print "i am %s,age is %s,my email is %s,%s" % (name[0],name[1],user['email'],str)
foo()

## 方法二：通过*args注入,适用于字符串和列表，感觉是第一种方式的变种  
def hello(fn):
	def wrapper(*args):
		print "hello, %s" % fn.__name__
		args =  ['lzp','123']
		return fn(*args)
	return wrapper
 
@hello
def foo(*args):
	print "i am %s,age is %s" % (args[0],args[1])

foo()

## 方法三：通过**kwargs注入,适用于字典，和args思想一致
def hello(fn):
	def wrapper(**kwargs):
		print "hello, %s" % fn.__name__
		kwargs = {'name':'lzp','age':18,'email':'lzp@126.com'}
		return fn(**kwargs)
	return wrapper
 
@hello
def foo(**kwargs):
	print "i am %s,my email is %s" % (kwargs['name'],kwargs['email'])

foo()

## 方法四：混合模式，回调函数将装饰器函数名当做参数传入，支持字符串，列表和字典
def hello(fn):
	def wrapper(*args,**kwargs):
		print "hello, %s" % fn.__name__
		name =  ['lzp','18']
		str = "lzp"
		user = {'name':'lzp','age':18,'email':'lzp@126.com'}
		#return fn(user,*args,**kwargs)    #一次只能返回一个参数，此处返回字典参数
		return fn(name,*args,**kwargs)     #返回列表参数
		#return fn(str,*args,**kwargs)     #返回字符串参数
	return wrapper
 
@hello
def foo(test):                                                     #回调函数任意定义一个参数名，来接受传来的值
#def foo(test,a,b='test'):                                         #可以同时接受其他形式的参数，但接受装饰器的参数必须在前面
#	print "i am %s,my email is %s" % (test['name'],test['email'])  #打印字典的返回值，结果：i am lzp,my email is lzp@126.com
	print "i am %s,my age is %s" % (test[0],test[1])               #打印列表的返回值，结果：i am lzp,age is 18
#	print "i am %s" % test                                         #打印字符串的返回值，结果：i am lzp

foo()
#foo('fuck')



##  装饰器本质探究 ##
#def fuck(fn):
#	def wrapper(*arg,**args):
#		print  "fuck %s!" % fn.__name__[::-1].upper()
#		fn(*arg,**args)
#		wrapper.__name__ = '%s' % fn.__name__
#	return wrapper
#
#@fuck
#def wfg(name):
#    print "hello %s" % name 
##@fuck
#def test(name):
#	'''fuck you 
#	'''
#	print "nimei %s" % name
#
#wfg('cjk')
#test('abc')
#print wfg.__name__
#print test.__name__
#print test.__doc__
#print __doc__
