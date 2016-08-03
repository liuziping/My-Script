#!/usr/bin/env python
# encoding=utf-8
import os,time

def ping_idc(ip):
    num = 0
    while True:
        result = os.system("ping -c 1 %s>/dev/null 2>&1" %ip)
        if result == 0:
            print  'pong'                            
            time.sleep(5)
        else:
            num += 1
            if num == 3:
                 print "%s not pong" % ip    
                 break;
if __name__=='__main__':
    ips=['182.18.40.227','182.18.40.226']
    for ip in ips:
       ping_idc(ip)
