from flask import render_template
from . import asset 

@asset.route('/server')
def server():
	return render_template('asset/server.html')
