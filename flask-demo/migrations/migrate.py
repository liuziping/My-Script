import os,json
from flask import Flask, render_template, session, redirect, url_for
from flask.ext.script import Manager, Shell
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://liuziping:liuziping_123456@192.168.1.251:3306/test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

manager = Manager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    age = db.Column(db.String(64))

    def __repr__(self):
        return '<User %r>' % self.username

def make_shell_context():
    return dict(app=app, db=db, User=User)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@app.errorhandler(404)
def page_not_found(e):
    return "this page is not exist"


@app.errorhandler(500)
def internal_server_error(e):
    return "server is too busy"


@app.route('/', methods=['GET', 'POST'])
def index():
	return "ok"

if __name__ == '__main__':
    manager.run()
