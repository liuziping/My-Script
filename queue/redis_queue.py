#coding:utf-8
import redis


class Task(object):
	def __init__(self):
		self.rcon = redis.StrictRedis(host='192.168.1.253',port=6379,db=3)
		self.queue = 'tast:test:queue'
	
	def listen_tesk(self):
		while True: 
			task = self.rcon.blpop(self.queue,0)[1] 
			print "Task get",task

if __name__ == '__main__':
	print "listen task queue"
	p = Task()
	p.listen_tesk()
