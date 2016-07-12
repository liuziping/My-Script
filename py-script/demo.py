#!/usr/bin/env python
#coding: utf-8

from flask import Flask

app = Flask(__name__)

@app.route('/user/<string:username>')    
def index(username):
      return 'welcome  %s' % username

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)
