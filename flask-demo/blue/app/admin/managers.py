from flask import render_template
from . import users 

@users.route('/managers')
def managers():
	return render_template('admin/managers.html')
