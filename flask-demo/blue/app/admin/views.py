from flask import render_template
from . import users 

@users.route('/')
def users():
	return render_template('admin/users.html')
