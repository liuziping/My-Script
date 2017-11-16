#coding:utf-8
import redis


class Task(object):
	def __init__(self):
		self.rcon = redis.StrictRedis(host='192.168.1.253',port=6379,db=3)
		self.ps = self.rcon.pubsub()
		self.ps.subscribe('task:pubsub:channel')
	
	def listen_tesk(self):
		for i in self.ps.listen():
			if i['type'] == 'message':
				print "Task get",i['data']

if __name__ == '__main__':
	print "listen  tast  channel"
	p = Task()
	p.listen_tesk()
