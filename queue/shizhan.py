#coding:utf-8
import redis
import json

class Redis():
	def __init__(self):
		self.rcon = redis.StrictRedis(host='192.168.1.253',port=6379,db=3)
		self.key = 'dict1'

	def insert(self,jsonstr):
		self.rcon.lpush(self.key,jsonstr)

	def get(self):
		arr = self.rcon.lrange(self.key,0,-1)
		for i in range(0,len(arr)):
			print arr[i]
			print type(arr[i])
			self.rcon.rpop(self.key)

if __name__ == '__main__':
	test = Redis()
	json = [{"id":"1","hostname":"test1","stdout":"just a test"},{"id":"2","hostname":"app","stdout":"app is ok"}]
	for item in json:
		test.insert(item)
 	test.get()


