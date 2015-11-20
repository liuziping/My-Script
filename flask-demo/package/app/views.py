from flask import render_template
from . import app 

@app.route('/views')
def views():
	return render_template('views.html')
