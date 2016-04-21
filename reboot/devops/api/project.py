#!/usr/bin/env python
#coding:utf-8
from flask import  request
from . import app , jsonrpc
from auth import auth_login
import json, traceback
import util
import time

#这里是关于项目的增删改查

@jsonrpc.method('project.create')
@auth_login
def project_create(auth_info, **kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    if '1' not in  auth_info['r_id']:
        return json.dumps({'code': 1,'errmsg':'you not admin,no power' })
    try:
        data = request.get_json()['params']
        if not data.has_key('principal'):     
            return json.dumps({'code':1,'errmsg':'must hava principal'})
        if not app.config['cursor'].if_id_exist('user',data['principal'].split(',')):     
            return json.dumps({'code':1,'errmsg':'principal not exist'})
        if data.has_key('p_uesr') and not app.config['cursor'].if_id_exist('user',data['p_uesr'].split(',')):     
            return json.dumps({'code':1,'errmsg':'p_user not exist'})
        if data.has_key('p_group') and not app.config['cursor'].if_id_exist('role',data['p_group'].split(',')):     
            return json.dumps({'code':1,'errmsg':'p_group not exist'})
        data['create_date'] = time.strftime('%Y-%m-%d %H:%M:%S')
        app.config['cursor'].execute_insert_sql('project', data)
        util.write_log('api').info(username, "create project %s scucess" %  data['name'])
        return json.dumps({'code':0,'result':'create project %s scucess' % data['name']})
    except:
        util.write_log('api').error(username,"create project error: %s" % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'create project fail'})

@jsonrpc.method('project.getlist')
@auth_login
def project_select(auth_info,**kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    if '1' not in auth_info['r_id']:
        return json.dumps({'code': 1,'errmsg':'you not admin,no power' })
    try:
        output = ['id','name','path','principal','p_user','p_group','is_lock','comment']
        data = request.get_json()['params']
        fields = data.get('output', output)
          
        #查询用户表，生成id2name的字典
        result = app.config['cursor'].get_results('user', ['id', 'name'])
        users = dict([(str(x['id']), x['name']) for x in result])

        #查询角色表，生成id2name的字典
        res = app.config['cursor'].get_results('role', ['id', 'name'])
        roles = dict([(str(x['id']), x['name']) for x in res])

        #查询项目表，把项目表中p_uesr,p_group,principal的ID 转为name
        projects = app.config['cursor'].get_results('project', fields)
        for p  in projects:  #principal是必选项，肯定有值，p_user,p_group允许为空，故在取值时用了get方法设置默认值
            p['principal'] = ','.join([ users[x] for x in  p['principal'].split(',') if x in users ])
            p['p_user'] =  ','.join([users[u] for u in p.get('p_user','0').split(',') if u in users])
            p['p_group'] =  ','.join([roles[r] for r in p.get('p_group','0').split(',')  if r in roles])


        util.write_log('api').info(username, 'select project list success')
        return json.dumps({'code':0,'result':projects,'count':len(projects)})
    except:
        util.write_log('api').error("select project list error: %s"  %  traceback.format_exc())
        return json.dumps({ 'code':1,'errmsg':'get projectlist failed'})

@jsonrpc.method('project.get')
@auth_login
def project_get(auth_info, **kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    try:
        output = ['id','name','path','principal','p_user','p_group','is_lock','comment']
        data = request.get_json()['params']
        fields = data.get('output', output)
        where = data.get('where',None)
        if not where:
            return json.dumps({'code':1, 'errmsg':'must need a condition'})
        result = app.config['cursor'].get_one_result('project', fields, where)
        if not result :
            return json.dumps({'code':1, 'errmsg':'result is null'})
        else:
            util.write_log('api').info(username, "select project by id success")
            return json.dumps({'code':0,'result':result})
    except:
        util.write_log('api').error('select project by id error: %s'  % traceback.format_exc())
        return  json.dumps({'c ode':1,'errmsg':'get project failed'})

@jsonrpc.method('project.update')
@auth_login
def project_update(auth_info, **kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    if '1' not in auth_info['r_id']:
        return json.dumps({'code': 1,'errmsg':'you not admin,no power' })
    try:
        data = request.get_json()['params']
        where = data.get('where',None)
        data = data.get('data',None)
        if not where:
            return json.dumps({'code':1, 'errmsg':'must need a condition'})
        result = app.config['cursor'].execute_update_sql('project', data, where)
        if not result:
            return json.dumps({'code':1, 'errmsg':'result is null'})
        util.write_log('api').info(username, 'update project success!' )
        return json.dumps({'code':0,'result':'update project scucess'})
    except:
        util.write_log('api').error("update error: %s"  % traceback.format_exc())
        return  json.dumps({'code':1,'errmsg':"update project failed "})

@jsonrpc.method('project.delete')
@auth_login
def project_delete(auth_info,**kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    if '1' not in auth_info['r_id']:
        return json.dumps({'code': 1,'errmsg':'you not admin,no power' })
    try:
        data = request.get_json()['params']
        where = data.get('where',None)
        if not where:
            return json.dumps({'code':1, 'errmsg':'must need a condition'})
        result = app.config['cursor'].execute_delete_sql('project', where)
        if not result :
            return json.dumps({'code':1, 'errmsg':'result is null'})
        util.write_log('api').info(username, 'delete project successed')
        return json.dumps({'code':0,'result':'delete project scucess'})
    except:
        util.write_log('api'). error('delete project error: %s' %  traceback.format_exc())
        return json.dumps({'co de':1,'errmsg':'delete project failed'}) 


#新添加查询某个用户所拥有的项目列表
@jsonrpc.method('userprojects.getlist')
@auth_login
def userprojects(auth_info,**kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)             
    username = auth_info['username']
    try:
        res = util.user_projects(username) #dict
        return json.dumps({'code': 0, 'result': res})
    except:
        util.write_log('api').error("调用userproject函数失败: %s" % traceback.format_exc())
        return json.dumps({'code': 1, 'errmsg': '查询项目列表错误'})
