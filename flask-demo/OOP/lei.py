#coding:utf-8
class Province:
	"""类的描述信息 """
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return "this is a test"

# 直接访问普通字段
obj = Province('河北省')
print obj.name
print obj 
