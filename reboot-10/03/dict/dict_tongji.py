#!/usr/bin/env python
#coding:utf-8

content="who have touched their lives Love begins with a smile grows with a kiss and ends with a tear The brightest future will always be based on a forgotten past yoes" 

result = {}
for s in content.split(" "):
    if s in result:          
        result[s] +=1       # result[s] = result.get(s,0)+1   get优化写法替换if else
    else:
        result[s] = 1 
print result
res  = {} 
for k,v in result.items():
    res.setdefault(v,[])    # dict.setdefault(k,v) 给字典设置默认值，对应的get,获取字典的默认值
    res[v].append(k)
print res 
