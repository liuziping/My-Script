from flask import Flask,request,render_template,redirect,url_for
import requests
app = Flask(__name__)
import json



@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True,port=9092,host='0.0.0.0')







