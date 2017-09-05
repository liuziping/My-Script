#!/usr/bin/env python
#coding:utf8
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

# 资源不存在时的返回
def abort_if_todo_doesnt_exist(todo_id):
	if todo_id not in todos:
		abort(404,message="todo {} doesn't exist".format(todo_id))

# 获取传入的变量task值
parser = reqparse.RequestParser()
parser.add_argument('task',type=str)

# 资源的查、改、删,需要传入id
class Todo(Resource):
    def get(self,todo_id):
		abort_if_todo_doesnt_exist(todo_id)
		return {todo_id:todos[todo_id]}

    def put(self,todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        args = parser.parse_args()
        print args 
        task = {'task':args['task']}
        todos[todo_id] = task
        return {todo_id:todos[todo_id]},201
        
    def delete(self,todo_id):
		abort_if_todo_doesnt_exist(todo_id)
		del todos[todo_id]
		return '',204

# 资源的查所有 添加,不需要传入id
class TodoList(Resource):
	def get(self):
		return todos

	def post(self):
		args = parser.parse_args()
		todo_id = str(int(max(todos))+1)
		todos[todo_id] = {'task':args['task']}
		return todos[todo_id],201

# 定义两个场景的访问路由
api.add_resource(Todo,'/<string:todo_id>')
api.add_resource(TodoList,'/')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=7777,debug=True)
