#!/usr/bin/env python
#coding:utf8
import pickle

# 增
def Create():
  users = {'pc':'123456','wd':'123','kk':'234'}
  fo=open('users.txt','wb')       # pickle模块是以二进制形式存储在文件中，故必须以二进制形式打开
  pickle.dump(users,fo)            # 将字典写入文件中
  fo.close()

# 删
def Delete():
  content = {}
  f= open('users.txt')               # 导入字典的时候不能用wb模式，
  content = pickle.load(f)          # 将文件导入到字典中
  f.close
  content.pop('kk')
  f= open('users.txt','wb')          #修改后的字典再次写入文件，文件必须以二进制形式打开
  pickle.dump(content,f)
  f.close()

# 改
def Modify():
  content = {}
  f= open('users.txt')               # 导入字典的时候不能用wb模式，
  content = pickle.load(f)          # 将文件导入到字典中
  f.close
  content['pc']='6666'
  f= open('users.txt','wb')          #修改后的字典再次写入文件，文件必须以二进制形式打开
  pickle.dump(content,f)
  f.close()

# 查
def Select():
  content = {}
  f= open('users.txt')
  content = pickle.load(f)
  f.close
  print content
  for k,v in content.items():
      print "用户信息：%s-->%s" % (k,v) 

Create()
Delete()
Modify()
Select()
