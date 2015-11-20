from flask import  Flask
from views import asset
from admin import users

app = Flask(__name__)

app.register_blueprint(asset,url_prefix='/asset')
app.register_blueprint(users,url_prefix='/admin')

