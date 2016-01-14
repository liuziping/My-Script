from flask import render_template,request
from . import main

@main.route('/',methods=['GET','POST'])
def index():
	return "just a test"
