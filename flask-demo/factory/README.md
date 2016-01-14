# 关于工厂函数的个人理解

##  嵌套函数的两种使用场景

###  工厂函数

```	
    cat  test.py
		def maker(M):
			def action(X):
				return X**M
			return action

		f = maker(3)           #实例化。相当于类了
		print f(2)

		python test.py
		8
```
>   python中的工厂函数看上去有点像函数，实质上他们是类，当你调用它们时，实际上是生成了该类型的一个实例，就像工厂生产货物一样.

###  装饰器

```
		cat  test.py 
		def hello(fn):
			def wrapper():
				print"hello, %s" % fn.__name__           #返回函数名，会返回传入的函数名 foo
				fn()                                     #执行传来的函数foo并返回函数结果，foo仅仅仅是wrappr的一个参数
				print"goodby, %s" % fn.__name__
			return wrapper                      

		@hello
		def foo():                                       #foo函数会被当成一个参数，拿到hello装饰器里运行
			print"i am foo"

		foo()
		python  test.py
		hello, foo
		 i am foo
		 goodby,foo
```

### 嵌套函数总结

*  嵌套函数书写格式

>  一个父函数里面嵌套一个子函数， 子函数return具体的命令操作，父函数return 子函数名 

* 工厂函数 vs  修饰器

	 * 工厂函数： 工厂生成一批初始化过的零件， 不同公司拿到后，贴上自己的商标（实例化），就变成了不同品牌的货物——工厂生成好零件，自己拿来贴上自己的商标
	 * 装饰器:   相当于一个商标厂，任何一个产品生成完成后，都需要到修饰器里贴一下商标才能使用——讲自己生成好的产品，送到商标处，商标厂商给贴商标 

