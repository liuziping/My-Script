from flask import Flask,render_template,session,flash,url_for
from app import app 
from .form import NameForm




@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404 
	    
		    
@app.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html'), 500 

@app.route('/', methods=['GET', 'POST'])
def index():

	form = NameForm()
	if form.validate_on_submit():
		session['name'] = form.username.data
		session['password'] = form.password.data
	return render_template('index.html', form=form, name=session.get('name'))

