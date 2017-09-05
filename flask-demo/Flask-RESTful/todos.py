from flask import Flask,request
from flask.ext.restful import Resource,Api,reqparse,abort
import json

app = Flask(__name__)
api = Api(app)

todos = {
	'1' : {'task':'build an API'},
	'2' : {'task':'build a web'},
	'3' : {'task':'build a app' }
}

def abort_if_todo_doesnt_exist(todo_id):
	if todo_id not in todos:
		print todo_id
		abort(404,message="todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task',type=str,help='Rate cannot be converted')

@app.route('/todo/<string:todo_id>/',methods=['GET','PUT','DELETE'])
def index(todo_id):
	if request.method == 'GET':
		abort_if_todo_doesnt_exist(todo_id)
		return json.dumps({todo_id:todos[todo_id]},indent=4)
	elif request.method == 'PUT':
		args = parser.parse_args()
		task = {'task':args['task']}
		todos[todo_id] = task
		return json.dumps({todo_id:todos[todo_id]},{'status_code':201},indent=4)
	elif request.method == 'DELETE':	
		del todos[todo_id]
		return '',204

@app.route('/todo/',methods=['GET','POST'])
def todo():
	if request.method == 'GET':
		return json.dumps(todos,indent=4)
	elif request.method == 'POST':
		args = parser.parse_args()
		todo_id = str(int(max(todos))+1)
		todos[todo_id] = {'task':args['task']}
		return json.dumps({'tast':todos[todo_id],'status_code':201},indent=4)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=7777,debug=True)
