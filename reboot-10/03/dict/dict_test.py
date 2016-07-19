#!/usr/bin/env python
content = {'name':'lyz','pc':[1,2,3],'woniu':{'age':31,'job':'IT'}}
for k,v in content.items():
    print k+':'
    if isinstance(v,dict):
        for a,b in v.items():
            print a,b
    elif isinstance(v,list):
        for c in v:
            print c
    else:
        print v
