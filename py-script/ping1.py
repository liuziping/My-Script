#!/usr/bin/env python
# encoding=utf-8
import ping

def ping_idc():
    is_null = lambda x : x if x != None else 0.0   # 如果x参数为空返回0.0，否则返回x参数
    result = []
    addr = ['182.18.40.226','182.18.40.227']
    for ip in addr:
        percent, mrtt, artt = ping.quiet_ping(ip)
        for metric, v in [('ping.alive', percent), ('ping.max_rtt', is_null(mrtt)), ('ping.avg_rtt', is_null(artt))]:
            x  = {
                  'metric': metric,
                  'value': v,
                  'host':ip
            }
            result.append(x)
    return result

if __name__ == '__main__':
    print ping_idc()


