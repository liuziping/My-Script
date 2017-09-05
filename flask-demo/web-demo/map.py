import urllib2
import json
key = 'q5mTrTGzCSVq5QmGpI9y18Bo'
ipurl = 'http://api.map.baidu.com/location/ip?ak='+key+'&coor=bd09ll&ip='
sqlarr = []
def getGeo(ip):
    try:
        u = urllib2.urlopen(ipurl+ip)
        page = json.load(u)
        if 'content' in page:
            point = page['content'].get('point')
            print 'ip %s has geoX %s and geoY %s' % (ip,point['x'],point['y']) 
    except:
        print 'error'
getGeo('202.198.16.3')
