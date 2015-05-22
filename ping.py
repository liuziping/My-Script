#!/usr/bin/env python
# encoding=utf-8
import os
ip = '211.147.4.100'
def pingip(ip):   
    n=0
    while True:
        data=os.system("ping -c 1 %s>/dev/null 2>&1" %ip)
        if data==0:
            return  'ok'
	    break;
        else:
	     n=n+1
	     #print n
             if n==5:
                 print '%s ping fail'% ip
		 break;
if __name__=='__main__':
   pingip(ip)
