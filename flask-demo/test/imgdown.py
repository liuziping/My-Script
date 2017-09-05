import requests


img_url='http://ww1.sinaimg.cn/bmiddle/6ba75546jw1ei9nuw4npuj20cs087wfo.jpg'

def test_request():
	img_name = 'test.jpg'

	r = requests.get(img_url)
#	with open(img_name,'wb') as f:
    f = open(img_name,'wb')
	for chunk in r.iter_content(chunk_size=1024):
		f.write(chunk)

			
if __name__ == '__main__':
    test_request()
