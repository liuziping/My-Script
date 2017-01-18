#coding:utf-8
from flask import  request
from . import app , jsonrpc
from auth import auth_login
import json, traceback
import utils

# 权限的增删改查

@jsonrpc.method('power.create')                                                                                                        
@auth_login
def create(auth_info,**kwargs):
    username = auth_info['username']
    if '1' not in auth_info['r_id']:
        return json.dumps({'code': 1,'errmsg':'you not admin,no power' })
    try:
        data = request.get_json()['params']
        app.config['db'].execute_insert_sql('power', data)
        utils.write_log('api').info("%s create power %s success"  % (username,data['name']))
        return json.dumps({'code':0,'result':'create %s success' %  data['name']})
    except:
        utils.write_log('api').error('create power error:%s' % traceback.format_exc())
        return json.dumps({'code':1,'errmsg': 'create power failed'})

@jsonrpc.method('power.delete')
@auth_login
def delete(auth_info,**kwargs):
    username = auth_info['username']
    if '1' not in  auth_info['r_id']:
        return json.dumps({'code': 1,'errmsg':'you not admin,no power' })
    try:
        data = request.get_json()['params']
        where = data.get('where',None)
        if not where:
            return json.dumps({'code':1,'errmsg':'must need a condition'})
        result = app.config['db'].get_one_result('power', ['name'], where)
        if not result:
            return json.dumps({'code':1,'errmsg':'data not exist'})
        app.config['db'].execute_delete_sql('power', where)
        utils.write_log('api').info("%s delete power  success" % username)
        return json.dumps({'code':0,'result':'delete power success'})
    except:
        utils.write_log('api').error("delete power error:%s" % traceback.format_exc())
        return json.dumps({'code':1,'errmsg': 'delete power failed'})


@jsonrpc.method('power.getlist')
@auth_login
def getlist(auth_info,**kwargs):
    username = auth_info['username']
    if '1' not in auth_info['r_id']:
        return json.dumps({'code': 1,'errmsg':'you not admin,no power' })
    try:
        output = ['id','name','name_cn','url','comment']
        data = request.get_json()['params']
        fields = data.get('output', output)
        result = app.config['db'].get_results('power', fields)
        utils.write_log('api').info('%s select permission list success' % username)
        return json.dumps({'code':0,'result':result,'count':len(result)})
    except:
        utils.write_log('api').error("get list permission error: %s"  %  traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'get power_list failed'})

@jsonrpc.method('power.get')
@auth_login
def getbyid(auth_info,**kwargs):
    username = auth_info['username']                                                                                             
    try:
        output = ['id','name','name_cn','url','comment']
        data = request.get_json()['params']
        fields = data.get('output', output)
        where = data.get('where',None)
        if not where:
            return json.dumps({'code':1, 'errmsg':'must need a condition'})
        result = app.config['db'].get_one_result('power', fields, where)
        if not result:
            return json.dumps({'code':1, 'errmsg':'data not exist'})
        utils.write_log('api').info('%s select permission by id successed!' % username)
        return json.dumps({'code':0, 'result':result})
    except:
        utils.write_log('api').error("select power by id error: %s" %  traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'get power failed'})


@jsonrpc.method('power.update')
@auth_login
def update(auth_info, **kwargs):
    username = auth_info['username']
    if '1' not in auth_info['r_id']:
        return json.dumps({'code': 1,'errmsg':'you not admin,no power' })
    try:
        data = request.get_json()['params']
        where = data.get('where',None)
        data = data.get('data',None)
        if not where:
            return json.dumps({'code':1, 'errmsg':'must need a condition'})
        result=app.config['db'].execute_update_sql('power', data, where)
        if not result: 
            return json.dumps({'code':1, 'errmsg':'data not exist'})
        utils.write_log('api').info("%s update power successed" % username )
        return json.dumps({'code':0,'result':'update power success'})
    except:
        utils.write_log('api').error("update error: %s" % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'update power failed'})



