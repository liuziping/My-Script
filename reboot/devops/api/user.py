#!/usr/bin/env python
#coding:utf-8
from flask import request
from . import app ,jsonrpc
import time, logging, util
from auth import auth_login
import json, traceback,hashlib

#本模块提供用户信息的增删改查，以及 用户所在组，所有权限的查询

#将字符串转为列表 传入的参数如[u'1,2'] or [u'1,2', u'1,3,4']，结果为['1','2','3','4']
def getid_list(ids):   
    if not isinstance(ids, list):
        return None
    id_list = []
    for x in ids:                #每次循环出x如：'1,2','2,3,4'   
        id_list +=x.split(',')   #将每次循环输出的字符串转为列表，并将列表合并
    id_list = set(id_list)       #将列表去重
    #print id_list
    return  id_list


#创建用户
@jsonrpc.method('user.create')
@auth_login
def createuser(auth_info,*arg,**kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    r_id = auth_info['r_id']    #string,  eg:  '1,2,3'
    if '1' not in r_id:         #角色id = 1 为sa组，超级管理员
        return json.dumps({'code': 1,'errmsg':'只有管理员才有此权限' })
    try:
        data = request.get_json()['params']
        #api端对传入端参数验证
        if 'r_id' not in data:
            return json.dumps({'code': 1, 'errmsg': "必须选择一个所属组!"})
        if not util.check_name(data['username']):
            return json.dumps({'code': 1, 'errmsg': "用户名必须为字母和数字!"})
        if data['password'] != data['repwd']:
            return json.dumps({'code': 1, 'errmsg': "两次输入的密码不一致!"})
        elif len(data['password']) < 6:
            return json.dumps({'code': 1, 'errmsg': '密码至少需要6位!'})
        else:
            data.pop('repwd')    #传入的第二次密码字段不存在，需要删除
        data['password'] = hashlib.md5(data['password']).hexdigest()
        data['join_date'] = time.strftime('%Y-%m-%d %H:%M:%S')
        app.config['cursor'].execute_insert_sql('user', data)

        util.write_log('api').info(username, "create_user %s" % data['username'])
        return json.dumps({'code': 0, 'result': '创建用户%s成功' % data['username']})
    except:
        util.write_log('api').error("Create user error: %s" % traceback.format_exc())
        return json.dumps({'code':  1, 'errmsg': '创建用户失败，有异常情况'})
#获取(uid or username)个人信息，个人信息展示和个人修改信息，以及用户列表中更新用户信息部分的获取数据
@jsonrpc.method('user.get')
@auth_login
def userinfo(auth_info,**kwargs):
    if auth_info['code'] ==  1:
        return  json.dump(auth_info)
    username = auth_info['username']
    try:
        output = ['id','username','name','email','mobile','role','is_lock','r_id']
        fields = kwargs.get('output',output) #api可以指定输出字段，如果没有指定output，就按默认output输出
        where = kwargs.get('where',None)     #前端传来的where条件，可能是uid或者username
        result = app.config['cursor'].get_one_result('user', fields, where)
        if result is '':
            return json.dumps({'code':1, 'errmsg':'必须选择一个用户'})
        util.write_log('api').info(username, 'get_one_user info') 
        return json.dumps({'code':0,'result':result})
    except:
        util.write_log('api').error("Get users list error: %s" % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'获取用户信息失败'})

'''
#获取用户信息
@jsonrpc.method('user.getinfo')
@auth_login
def userselfinfo(auth_info,**kwargs):
    if auth_info['code'] ==  1:
        return  json.dump(auth_info)
    username = auth_info['username']
    fields = ['id','username','name','email','mobile','role','is_lock','r_id']
    try:
        user = app.config['cursor'].get_one_result('user', fields, where={'username': username})
        if user.get('r_id', None):
            r_id = user['r_id'].split(',')

            #获取组所有的id,name并存为字典如：{'1': 'sa', '2': 'php'}
            gids = app.config['cursor'].get_results('user_group', ['id', 'name', 'p_id'], where={'id': r_id})
        else:
            gids = {}
        own_pids = set([])
        for x in gids:
                own_pids |= set(x['p_id'].split(','))
        user['r_id'] = [x['name'] for x in gids]

        if own_pids:
            pids = app.config['cursor'].get_results('permission', ['id', 'name', 'name_cn', 'url'], where={'id': list(own_pids)})
            user['p_id'] = dict([(str(x['name']), dict([(k, x[k]) for k in ('name_cn', 'url')])) for x in pids])
        else:
            user['p_id'] = {}

        util.write_log(username, 'get_user_info')
        return  json.dumps({'co de': 0, 'user': user})
    except:
        logging.getLogger().error("Get users list error: %s" % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'获取用户信息失败'})

#获取用户列表
@jsonrpc.method('user.getlist')
@auth_login
def userlist(auth_info,**kwargs):
    if auth_info['code'] ==  1:
        return  json.dump(auth_info)
    username = auth_info['username']
    r_id = auth_info['r_id'])
    users = []
    fields = ['id','username','name','email','mobile','role','is_lock','r_id']
    try:
        if '1' not in r_id:
            return json.dumps({'code': 1,'errmsg':'只有管理员才有此权限' })
        #获取组所有的id,name并存为字典如：{'1': 'sa', '2': 'php'}
        #gids = app.config['cursor'].get_results('user_group', ['id', 'name'])
        #gids = dict([(str(x['id']), x['name']) for x in gids])
        result = app.config['cursor'].get_results('user', fields)
        for user in result: #查询user表中的r_id,与user_groups表生成的字典对比，一致则将id替换为name,如，"sa,php"
            user['r_id'] = ','.join([gids[x] for x in user['r_id'].split(',') if x in gids])
            users.append(user)
        util.write_log(username, 'get_all_users')
         return  json.dumps({'code': 0, 'users': users,'count':len(users)})
    except:
        logging.getLogger().error("Get users list error: %s" % traceback.format_exc())
         return json.dumps({'code':1,'errmsg':'获取用户列表失败'})
 
#更新用户信息
@jsonrpc.method('user.update')
@auth_login
def userupdate(auth_info, **kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    if auth_info['role'] != '0':
        return json.dumps({'code':1,'errmsg':'只有管理员才有此权限'})
    try:
        data = request.get_json()['params']
        where = data.get('where',None)
        data = data.get('data',None)
        print data,where
        if int(auth_info['role']) == 0:
            result = app.config['cursor'].execute_update_sql('user', data, where)
        else:
            result =  app.config['cursor'].execute_update_sql('user', data, where,['name','username','email','mobile'])
        if result == '':
            return json.dumps({'code':1, 'errmsg':'需要指定一个用户'})
        util.write_log(username, 'update groups %s success!' % data['name'])
        return  json.dumps({'code':0,'result':'更新用户%s成功' % data['name']})
    except:
        logging.getLogger().error("update error: %s"  % traceback.format_exc())
        return json.dumps({'code':1, 'errmsg':"更新用户失败"})


#删除用户
@jsonrpc.method('user.delete')
@auth_login
def userdelete(auth_info, **kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    if auth_info['role'] != '0':
        return json.dumps({'code':1,'errmsg':'只有管理员才有此权限'})
    try: 
        data = request.get_json()['params']
        result = app.config['cursor'].execute_delete_sql('user', data)
        if result == '':
            return json.dumps({'code':1,'errmsg':'需要指定一个用户'})
        util.write_log(username, 'delete user successed')
        return json.dumps({'code':0,'result':'删除用户成功'})
    except:
        logging.getLogger().error('delete groups error: %s' %  traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'删除用户失败'})


#修改密码
@app.route('/api/password',methods=['PUT'])
@auth_login
def passwd(auth_info):
    if auth_info['code'] == 1:   #主要用于判断认证是否过期，过期会会在web提示
        return json.dumps(auth_info)
    username = auth_info['username']
    uid = int(auth_info['uid'])
    role = int(auth_info['role'])
    try:
         data = request.get_json()
        if role==0 and 'user_id' in data:   # admin no need oldpassword  but need user_id
            user_id = data['user_id']
            if not app.config['cursor'].if_userid_exist(user_id): 
                return json.dumps({'code':1,'errmsg':'需要更改密码的用户不存在'})
            password = hashlib.md5(data['password']).hexdigest()
            app.config['cursor'].execute_update_sql('user', {'password': password}, {'id': user_id})
        else:                  #user  need input oldpassword
            if not data.has_key("oldpassword") :
                return json.dumps({'code':1,'errmsg':'需要提供原密码'})
            oldpassword = hashlib.md5(data['oldpassword']).hexdigest()
            res = app.config['cursor'].get_one_result('user', ['password'], {'username': username})
            if res['password'] != oldpassword:
                return json.dumps({'code':1,'errmsg':'原密码输入有误'})
            password = hashlib.md5(data['password']).hexdigest()
            app.config['cursor'].execute_update_sql('user', {'password': password}, {'username': username})

        if not git_passwd(username, data['password']):
            return json.dumps({'code': 1, 'errmsg': 'Git密码更新失败，请联系管理员'})
        util.write_log(username,'update user password')
        return json.dumps({'code':0,'result':'更新密码成功'})
    except:
        logging.getLogger().error('update user password error : %s' % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'更新密码有异常'})


#用户登录成功后通过用户username获取自己的权限信息，个人中心用户权限部分使用，点击权限名会连接到响应的url
@jsonrpc.method('user_perm.getlist')
@auth_login
def getlist(auth_info,**kwargs):
    if auth_info['code']==1:
        return json.dumps(auth_info)
    username = auth_info['username']
    id = auth_info['uid']
    try:
        output = ['name','name_cn','url','info']
        fields = kwargs.get('output', output)

        res = app.config['cursor'].get_one_result('user', ['r_id'], {'username': username})
        r_id = getid_list([res['r_id']])

        res = app.config['cursor'].get_results('group', ['p_id'], {'id': r_id})
        perm_result = getid_list([x['p_id'] for x in res])

        result = app.config['cursor'].get_results('permission', fields, {'id': perm_result})
        util.write_log(username, "get permission success")
        return json.dumps({'resu lt':0,'result':result,'count':len(result)})
    except:
        logging.getLogger().error("get list permission error: %s"  %  traceback.format_exc())
        return json.dumps({'cod e':1,'errmsg':'获取权限列表失败'})

#用户登录成功后通过用户username获取自己的组信息，个人中心调用
@jsonrpc.method('user_groups.getlist')
@auth_login
def user_groups(auth_info, **kwargs):
    if auth_info['code'] == 1: 
        return json,dumps(auth_info)
    username = auth_info['username']
    try:
        output = ['id','name','name_cn','p_id','info']
        fields = kwargs.get('output', output)

        res = app.config['cursor'].get_one_result('user', ['r_id'], {'username': username})
        r_id= getid_list([res['r_id']])

        result = app.config['cursor'].get_results('user_group', fields, {'id': r_id})
        util.write_log(username, "get groups success")
        return json.dumps({'code':0,'result':result,'count':len(result)})
    except:
        logging.getLogger().error("get list groups error: %s"  % traceback.format_exc())
        return json.dumps({'code':1, 'errmsg':'获取组列表失败'})
'''
