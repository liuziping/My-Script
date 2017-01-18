from flask import Flask
from config import *
from config1 import getconfig
import os

app = Flask(__name__)

app.config['HOST']='www.reboot.com'

#app.config.from_envvar('CONFIG_SET') 

# app.config.from_object(ProductionConfig)
#if os.path.exists("./online"):
#    app.config.from_object(config['pro'])
#elif os.path.exists("./dev"):
#    app.config.from_object(config['dev'])
#else:
#    app.config.from_object(config['dev'])

# app.config.from_pyfile('config1.py') 


conf = getconfig('test.conf','web')
app.config.update(conf)

print app.config 

@app.route('/')
def hello_world():
    return 'Hello World! %s,%s' % (app.config.get('HOST'),app.config['port'])  # app.config['key']

if __name__ == '__main__':
    app.run()
