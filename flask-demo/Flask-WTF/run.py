from app import app
from app import manager

if __name__ == '__main__':
#    manager.run()
    app.run(host="0.0.0.0",port=9988,debug=True)
