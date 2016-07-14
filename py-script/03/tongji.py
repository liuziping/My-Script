#!/usr/bin/env python
#coding:utf-8

content="who have touched their lives Love begins with a smile grows with a kiss and ends with a tear The brightest future will always be based on a forgotten past you can’t go on well in lifeuntil you let go of your past failures and heartaches"

# 将文本拼接成word:num的字典形式
result = {}
for s in content.split(" "):
    if s in result:
        result[s] +=1
    else:
        result[s] = 1
#print result

# 字典翻转拼接为num:word的字典
res  = {}
for k,v in result.items():
    res.setdefault(v,[])
    res[v].append(k)
#print res


count = 0
f = open('tongji.html','a+')
f.write("<html><table style='border:solid 1px'>")
f.write("<th style='border:solid 1px'>次数</th><th style='border:solid 1px'>单词</th>")
while count < 4:
    key = max(res.keys())
    print "出现了%s次的单词：%s" % (key,res[key])
    for word in res[key]:
        f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (key,word))
    res.pop(key)
    count = count +1
f.write("</table></html>")
f.close()
