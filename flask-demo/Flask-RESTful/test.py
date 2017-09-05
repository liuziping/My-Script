# !/usr/bin/env python
# -*- coding: utf-8 -*-

# from flask import Flask
# from flask.ext import restful
#
# app = Flask(__name__)
# api = restful.Api(app)
#
# class HelloWorld(restful.Resource):
#     def get(self):
#         return {'hello': 'world'}
#
# api.add_resource(HelloWorld, '/')
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
# # =========================================
#
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return {'hello': 'world'}
#
# if __name__ == '__main__':
#     app.run(debug=True)




















# ============================
#
# from flask import Flask
# from flask.ext.restful import reqparse, Api, Resource, fields, marshal_with
#
# app = Flask(__name__)
# api = Api(app)
#
# # 1. 关于参数解析的部分
# # 一组虚拟的数据
# TODOS = {
#     'todo1': {'task': 1},
#     'todo2': {'task': 2},
#     'todo3': {'task': 3},
# }
#
# # 定义允许的参数为task，类型为int，以及错误时的提示
# parser = reqparse.RequestParser()
# parser.add_argument('task', type=int, help='Please set a int task content!')
#
# # 真正处理请求的地方
# class TodoList(Resource):
#     def get(self):
#         return TODOS, 200, {'Etag': 'some-opaque-string'}
#
#     def post(self):
#         args = parser.parse_args()
#         todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
#         todo_id = 'todo%i' % todo_id
#         TODOS[todo_id] = {'task': args['task']}
#         return TODOS[todo_id], 201
#
# # 实际定义路由的地方
# api.add_resource(TodoList, '/todos', '/all_tasks')
#
# # 2. 关于响应域的部分
# # ORM的数据模型
# class TodoDao(object):
#     def __init__(self, todo_id, task):
#         self.todo_id = todo_id
#         self.task = task
#
#         # 这个域不会被返回
#         self.status = 'active'
#
# # marshal-蒙版
# resource_fields = {
#     'task':   fields.String,
#     'uri':    fields.Url('todo_ep')
# }
#
# # 真正处理请求的地方
# class Todo(Resource):
#     # 蒙版
#     @marshal_with(resource_fields)
#     def get(self, todo_id):
#         return TodoDao(todo_id=todo_id, task='Remember the milk'), 200
#
# # 实际定义路由的地方
# api.add_resource(Todo, '/todos/<todo_id>', endpoint='todo_ep')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)














# =======================
#
# from flask import Flask
# from flask.ext.restful import reqparse, Api, Resource
#
# app = Flask(__name__)
# api = Api(app)
#
# USERS = {
#     'row1': {'name': 'jilu', 'rate': [70, 65]},
#     'row2': {'name': 'bob', 'rate': [80, 90, 68]},
#     'row3': {'name': 'tim', 'rate': [90, 80]},
# }
#
# parser = reqparse.RequestParser()
# parser.add_argument('name', type=str, required=True)
# parser.add_argument('rate', type=int, help='rate is a number', action='append')
# parser.add_argument('User-Agent', type=str, location='headers')
#
# # # 解析器继承
# parser_copy = parser.copy()
# parser_copy.add_argument('bar', type=int)
# parser_copy.replace_argument('bar', type=str, required=True)
# parser_copy.remove_argument('User-Agent')
#
# # 真正处理请求的地方
# class UserInfo(Resource):
#     def get(self):
#         return USERS, 200
#
#     def post(self):
#         # args = parser.parse_args()
#         args = parser_copy.parse_args()
#         user_id = int(max(USERS.keys()).lstrip('row')) + 1
#         user_id = 'row%i' % user_id
#         USERS[user_id] = {'name': args['name'], 'rate': args['rate']}
#         USERS[user_id]['ua'] = args.get('User-Agent')
#         USERS[user_id]['bar'] = args.get('bar')
#         return USERS[user_id], 201
#
# api.add_resource(UserInfo, '/')
#
# if __name__ == '__main__':
#     app.run(debug=True)





import json
from datetime import datetime

from flask.ext.restful import Resource, fields, marshal_with, marshal

# 基本例子
resource_fields = {
    'name': fields.String,
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc822'),
}

class UserInfo(object):
    def __init__(self, name, address, date_updated=datetime.now()):
        self.name = name
        self.address = address
        self.date_updated = date_updated


print json.dumps(marshal(UserInfo('magi', 'beijing'), resource_fields))

#
# class Todo(Resource):
#     @marshal_with(resource_fields, envelope='resource')
#     def get(self, **kwargs):
#         return UserInfo('magi', 'beijing')



# 输出域别名
resource_fields2 = {
    'open_name': fields.String(attribute='name'),
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc822'),
}

print json.dumps(marshal(UserInfo('magi', 'beijing'), resource_fields2))


# 输出域默认值
class UserInfo2(object):

    def __init__(self, address):
        self.address = address

resource_fields3 = {
    'open_name': fields.String(default='add_magi'),
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc822', default=str(datetime.now())),
}

print json.dumps(marshal(UserInfo2(address='beijing'), resource_fields3))


# 自定义输出域
class UserInfo2(object):

    def __init__(self, address, flag, date_updated=datetime.now()):
        self.address = address
        self.date_updated = date_updated
        self.flags = flag

class UrgentItem(fields.Raw):
    def format(self, value):
        return "Urgent" if value & 0x01 else "Normal"

resource_fields4 = {
    'open_name': fields.String(default='add_magi'),
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc822'),
    'priority': UrgentItem(attribute='flags'),
}

print json.dumps(marshal(UserInfo2(address='beijing', flag=0), resource_fields4))


# 复杂结构
resource_fields = {'name': fields.String}
resource_fields['address'] = {}
resource_fields['address']['line 1'] = fields.String(attribute='addr1')
resource_fields['address']['line 2'] = fields.String(attribute='addr2')
resource_fields['address']['city'] = fields.String
resource_fields['address']['state'] = fields.String
resource_fields['address']['zip'] = fields.String
data = {'name': 'bob', 'addr1': '123 fake street', 'addr2': '', 'city': 'New York', 'state': 'NY', 'zip': '10468'}
print json.dumps(marshal(data, resource_fields))

# 嵌套域
address_fields = {}
address_fields['line 1'] = fields.String(attribute='addr1')
address_fields['line 2'] = fields.String(attribute='addr2')
address_fields['city'] = fields.String(attribute='city')
address_fields['state'] = fields.String(attribute='state')
address_fields['zip'] = fields.String(attribute='zip')

resource_fields = {}
resource_fields['name'] = fields.String
resource_fields['billing_address'] = fields.Nested(address_fields)
resource_fields['shipping_address'] = fields.Nested(address_fields)
address1 = {'addr1': '123 fake street', 'city': 'New York', 'state': 'NY', 'zip': '10468'}
address2 = {'addr1': '555 nowhere', 'city': 'New York', 'state': 'NY', 'zip': '10468'}
data = { 'name': 'bob', 'billing_address': address1, 'shipping_address': address2}

print json.dumps(marshal(data, resource_fields))

#
#
#
#
#














