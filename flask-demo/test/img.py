"""
test different image download profile
"""

import requests
import StringIO
import cStringIO
from PIL import Image
import profile

img_url='http://ww1.sinaimg.cn/bmiddle/6ba75546jw1ei9nuw4npuj20cs087wfo.jpg'

def test_request():
    img_name = 'request.jpg'

    r = requests.get(img_url)
    with open(img_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)

def test_StringIO():
    img_name = 'stringio.jpg'

    r = requests.get(img_url)

    i = Image.open(StringIO.StringIO(r.content))
    i.save(img_name)

def test_cStringIO():
    img_name = 'cstringio.jpg'

    r = requests.get(img_url)

    i = Image.open(cStringIO.StringIO(r.content))
    i.save(img_name)

def test_request1():
    img_name = 'd_req.jpg'

    r = requests.get(img_url)
    with open(img_name,'wb') as f:
        f.write(r.content)

if __name__ == '__main__':
    profile.run('test_request()')
    #profile.run('test_StringIO()')
    #profile.run('test_cStringIO()')
    #profile.run('test_request1()')
