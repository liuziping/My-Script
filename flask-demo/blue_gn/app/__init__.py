from flask import  Flask
from views import asset

app = Flask(__name__)

app.register_blueprint(asset,url_prefix='/asset')

