from flask import Flask,request,render_template,redirect
import requests
import json


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<htmlname>')
def user(htmlname):
    return render_template(htmlname +'.html')

@app.route('/project/<htmlname>')
def project(htmlname):
    return render_template(htmlname +'.html')

@app.route('/cmdb/<htmlname>')
def cmdb(htmlname):
    return render_template(htmlname +'.html')

if __name__ == '__main__':
    app.run(debug=True,port=9888,host='0.0.0.0')







