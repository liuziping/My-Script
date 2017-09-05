import random
import struct
import uuid
import requests
"""
{'server_disk': '9', 
'uuid': 'DBBF5FD4-F293-46D0-B803-8DE4FF7D9E66', 
'server_type': 'VirtualBox', 
'server_cpu': 'Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1', 
'hostname': 'opsweb-django', 
'vm_status': 1, 
'manufacturers': 'innotek GmbH', 
'inner_ip': '192.168.99.10', 
'server_mem': '490.39 MB', 
'mac_address': '08:00:27:f6:45:f0', 
'manufacture_date': '2006-12-01', 
'os': 'CentOS 6.6 Final', 
'sn': '0'}
"""

def get_mac_address():
    mac_bin_list = []
    mac_hex_list = []
    for i in range(1,7):
        i = random.randint(0x00,0xff)
        mac_bin_list.append(i)
    Fake_HW = struct.pack("BBBBBB",mac_bin_list[0], mac_bin_list[1], mac_bin_list[2], mac_bin_list[3], mac_bin_list[4], mac_bin_list[5])
    for j in mac_bin_list:
        mac_hex_list.append(hex(j))
    Hardware = ":".join(mac_hex_list).replace("0x","")
    return Hardware

def get_uuid():
    return str(uuid.uuid1())

def get_hostname(): 
    for idc in ["yz", "zw", "jxq", "tj", "ct"]:
        for bus in ["fang", "zp", "sec", "service", "pay"]:
            for ser in ["web", "wap", "app", "api"]:
                for ind in range(1,10):
                    index = '{:0>2}'.format(ind)
                    hostname = "{}-{}-{}-{}".format(idc, bus, ser, index)
                    yield hostname

def get_ip_address():
    ip_ = "10.20"
    for ip3 in range(1,254,3):
        for ip4 in range(1,254,2):
            ip = "{}.{}.{}".format(ip_, ip3,ip4)
            yield ip

def run():
    hostname = get_hostname()
    ip = get_ip_address()
    data = {}
    data['server_disk'] = "9"
    data['server_type'] = "VirtualBox"
    data['server_cpu'] = "Intel(R) Core(TM) i5-4278U CPU @ 2.60GHz 1"
    data['vm_status'] = 1
    data['manufacturers'] = 'innotek GmbH'
    data['server_mem'] = '490.39 MB'
    data['manufacture_date'] = '2006-12-01'
    data['os'] = 'CentOS 6.6 Final'
    data['sn'] = '0'
    for i in range(1,200):
        data['uuid'] = get_uuid() 
        data['mac_address'] = get_mac_address()
        data['hostname'] = hostname.next()
        data['inner_ip'] = ip.next()
        send(data)
        

def send(data):
    print data
    url = "http://127.0.0.1:8800/server/server_add/"
    r = requests.post(url, data=data)


if __name__ == "__main__":
    run()
