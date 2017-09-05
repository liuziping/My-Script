from flask import Flask

app=Flask(__name__)

@app.route('/',endpoint='index')
def index():
	print "fuck you"

@app.route('/',endpoint='index')
def index():
	print "fuck you"

#@app.route('/test',endpoint='test')
#def index():
#	print "game over"
