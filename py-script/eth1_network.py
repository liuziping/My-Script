#!/usr/bin/env python
# coding: utf-8
import json
import time

try:
    import psutil
except ImportError:
    print('Error: psutil module not found!')
    exit()

# 函数获取各网卡发送、接收字节数
def get_key():
    key_in fo = psutil.net_io_counters(pernic=True).keys()  # 获取网卡名称,以列表存储
    recv = {}
    sent = {}
    for key in key_info:
        rec v.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)  # 0网卡接收的字节数
        sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)  # 网卡发送的字节数
    return key_info, recv, sent

# 函数计算每2秒速率
def get_rate():
    key_info, old_recv, old_sent = get_key()  # 上2秒收集的数据
    time.sleep(2)
    key, now_recv, now_sent = get_key()       # 当前所收集的数据
    net_in = {}
    net_out = {}
    for key in key_info:
        net_i n.setdefault(key, (now_recv.get(key) - old_recv.get(key)) / 1024)  # 每2秒接收速率
        net_out.setdefault(key, (now_sent.get(key) - old_sent.get(key)) / 1024) # 每2秒发送速率
    return key_info, net_in, net_out

while 1:
    try:
         key _info, net_in, net_out = get_rate()
         for key in key_info:
              if key == "eth1":    # 只打印某个网卡的数据 
                 data = {"key":key,"net_in":net_in.get(key),"net_out":net_out.get(key)}
                 data = json.dumps(data)
                 cmd =  "echo '%s'|nc 192.168.1.128 8888" % data
                 os.system(cmd)   
    except KeyboardInterrupt:
         exit()

