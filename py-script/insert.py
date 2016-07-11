#!/usr/bin/env python
#coding:utf-8

data = [8,5,9,3]
n = len(data)

for i in range(1,n):
    while  i > 0 and data[i] <  data[i-1]:
            data[i],data[i-1] = data[i-1],data[i]
            i = i - 1
print data

# 第一圈循环，i = 1,data[i] = 5 data[i-1]=8 执行替换
# [5,8,9,3]    i = 0 跳出while,开始第二圈循环

# 第二圈循环，i = 2  data[i]=9 > data[i-1]=8 不替换
# [5,8,9,3]

# 第三圈循环，i = 3,data[i]=3,data[i-1]=9,符合while条件
# 第一轮结果，[5,8,3,9], i=i-1, i=2,data[i]=3,data[i-1]=8,符合while
# 第二轮结果，[5,3,8,9], i=i-1, i=1,data[i]=3,data[i-1]=5,符合while
# 第三轮结果，[3,5,8,9], i=i-1, i=0,不符合while，game over
