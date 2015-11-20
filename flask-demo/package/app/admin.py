from flask import render_template
from . import app

@app.route('/admin')
def admin():
	return render_template('admin.html')
