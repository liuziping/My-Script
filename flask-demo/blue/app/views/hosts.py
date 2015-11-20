from flask import render_template
from . import asset 

@asset.route('/')
def host():
	return render_template('asset/host.html')
