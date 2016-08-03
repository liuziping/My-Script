#!/usr/bin/env python
# encoding=utf-8
import ping

def ping_idc():
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


