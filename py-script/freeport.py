#!/usr/bin/env  python
#coding:utf8
def findFreePort():
  """
  如果在bind绑定的时候指定端口0，意味着由系统随机选择一个可用端口来绑定
  函数返回值是当前可用来监听的一个随机端口。
  from pc  http://zhuanlan.zhihu.com/auxten/20365900

  """
  import socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(('localhost', 0))
  # 用getsockname来获取我们实际绑定的端口号
  addr, port = s.getsockname()
  # 释放端口
  s.close()
  return port

print findFreePort.__doc__
print findFreePort()
