#!/usr/bin/env python
#coding:utf-8
from flask import  request
from . import app , jsonrpc
from auth import auth_login
import json, traceback
import util

# 权限的增删改查

@jsonrpc.method('power.create')
@auth_login
def create(auth_info,**kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    if '1' not in auth_info['r_id']:
        return json.dumps({'code': 1,'errmsg':'只有管理员才有此权限' })
    try:
        data = request.get_json()['params']
        if not util.check_name(data['name']):
            return json.dumps({'code': 1, 'errmsg': '权限名必须为字母和数字'})
        app.config['cursor'].execute_insert_sql('power', data)
        util.write_log('api').info(username, "create power %s success"  %  data['name'])
        return json.dumps({'code':0,'result':'创建权限%s成功' %  data['name']})
    except:
        util.write_log('api').error('create power error:%s' % traceback.format_exc())
        return json.dumps({'code':1,'errmsg': '创建权限失败'})

@jsonrpc.method('power.delete')
@auth_login
def delete(auth_info,**kwargs):
    if auth_info['code']==1:
        return json.dumps(auth_info)
    username = auth_info['username']
    if '1' not in  auth_info['r_id']:
        return json.dumps({'code': 1,'errmsg':'只有管理员才有此权限' })
    try:
        data = request.get_json()['params']
        where = data.get('where',None)
        if not where:
            return json.dumps({'code':1,'errmsg':'需要指定一个权限'})
        result = app.config['cursor'].get_one_result('power', ['name'], where)
        if not result:
            return json.dumps({'code':1,'errmsg':'你传入条件的记录不存在'})
        app.config['cursor'].execute_delete_sql('power', where)
        util.write_log('api').info(username, "delete power  success")
        return json.dumps({'code':0,'result':'删除权限成功'})
    except:
        util.write_log('api').error("delete power error:%s" % traceback.format_exc())
        return json.dumps({'code':1,'errmsg': '删除权限失败'})

@jsonrpc.method('power.getlist')
@auth_login
def getlist(auth_info,**kwargs):
    if auth_info['code']==1:
        return json.dumps(auth_info)
    username = auth_info['username']
    if '1' not in auth_info['r_id']:
        return json.dumps({'code': 1,'errmsg':'只有管理员才有此权限' })
    try:
        output = ['id','name','name_cn','url','comment']
        data = request.get_json()['params']
        fields = data.get('output', output)
        result = app.config['cursor'].get_results('power', fields)
        util.write_log('api').info(username, 'select permission list success')
        return json.dumps({'code':0,'result':result,'count':len(result)})
    except:
        util.write_log('api').error("get list permission error: %s"  %  traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'获取权限列表失败'})

@jsonrpc.method('power.get')
@auth_login
def getbyid(auth_info,**kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    if '1' not in auth_info['r_id']:
        return json.dumps({'code': 1,'errmsg':'只有管理员才有此权限' })
    try:
        output = ['id','name','name_cn','url','comment']
        data = request.get_json()['params']
        fields = data.get('output', output)
        where = data.get('where',None)
        if not where:
            return json.dumps({'code':1, 'errmsg':'需要传入一个条件'})
        result = app.config['cursor'].get_one_result('power', fields, where)
        if not result:
            return json.dumps({'code':1, 'errmsg':'传入的条件没有查询结果'})
        util.write_log('api').info(username,'select permission by id successed!')
        return json.dumps({'code':0, 'result':result})
    except:
        util.write_log('api').error("select permission by id error: %s" %  traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'获取权限信息失败'})


@jsonrpc.method('power.update')
@auth_login
def update(auth_info, **kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    if '1' not in auth_info['r_id']:
        return json.dumps({'code': 1,'errmsg':'只有管理员才有此权限' })
    try:
        data = request.get_json()['params']
        where = data.get('where',None)
        data = data.get('data',None)
        result=app.config['cursor'].execute_update_sql('power', data, where)
        if not result: 
            return json.dumps({'code':1, 'errmsg':'需要指定一个权限'})
        util.write_log('api').info(username,"update power successed" )
        return json.dumps({'code':0,'result':'更新权限信息成功'})
    except:
        util.write_log('api').error("update error: %s" % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'更新权限失败'})
