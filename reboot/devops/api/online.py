#!/usr/bin/env python
#coding: utf-8
from flask import  request
from . import app, jsonrpc
import logging, time
import json, traceback
from auth import auth_login
import util

def apply_pub(username,data,where):
    #更新project_apply表
    app.config['cursor'].execute_update_sql('project_apply',data,where)
    util.write_log('api').info(username,"success and update project_apply status %s" % data['status'])

    #同时将本次操作插入到project_deploy中
    fields = ['project_id','info','applicant','status','apply_date','version','commit','detail']  
    result=app.config['cursor'].get_one_result('project_apply',fields,where)
    app.config['cursor'].execute_insert_sql('project_deploy',result)
    util.write_log('api').info(username,"success and insert project_deploy status  %s"  % data['status'])

#创建申请任务列表
@jsonrpc.method('apply.create') 
@auth_login
def apply_create(auth_info, **kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    if '1' not in auth_info['r_id']:
        return json.dumps({'code': 1,'errmsg':'you not admin,no power' })
    r_id = auth_info['r_id']
    field = ['project_id','info','applicant','commit','apply_date','status','detail']
    try:
        data = request.get_json()['params']  #project_id,project_name,applicant,info,detail
        data['commit']='11111'               #脚本获取
        data['apply_date'] = time.strftime('%Y-%m-%d %H:%M')
        data['status'] = 1
        data['applicant'] = username 
        where = {"project_id":int(data['project_id'])}
        data.pop('project_username')  
        res = app.config['cursor'].get_one_result('project_apply',field,where)
        if not res: 
            app.config['cursor'].execute_insert_sql('project_apply', data)
        else:
            app.config['cursor'].execute_update_sql('project_apply',data,where)
        app.config['cursor'].execute_insert_sql('project_deploy',data)  
        util.write_log('api').info(username,{'code':0,'result':'项目申请成功'})
        return json.dumps({'code':0,'result':'项目申请成功'})    
    except:
        util.write_log('api').error('project apply error: %s' % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'项目申请失败'})


#申请列表，任务列表
@jsonrpc.method('apply.getlist')
@auth_login
def apply_list(auth_info,**kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    try:
        output = ['id','project_id','info','applicant','version','apply_date','commit','status','detail']
        data = request.get_json()['params']  
        fields = data.get('output', output)
        applyer = app.config['cursor'].get_results('project_apply',fields)   #申请人看到的项目列表
        for res in applyer:
            res['apply_date']=str(res['apply_date'])

        where = {'status':['1','2']}
        result = app.config['cursor'].get_results('project_apply',fields,where) #只列出申请中和审核中的项目给发布者
        #id转换成名字
        id2name_project=util.getinfo('project',['id','name'])
        for res in result:
            res['project_name'] = id2name_project[str(res['project_id'])]           
            res['apply_date']=str(res['apply_date'])

        util.write_log('api').info(username, 'get apply list success!')
        return  json.dumps({'code':0,'data': applyer, 'result':result,'count':len(result)})
    except:
        util.write_log('api').error("select apply list error:%s" % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'任务列表获取失败!'})

#申请列表，详情按钮
@jsonrpc.method('apply.get')
@auth_login
def apply_one(auth_info,**kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    try:
        data = request.get_json()['params']
        output = ['id','project_id','info','applicant','version','commit','apply_date','status','detail']
        fields = data.get('output', output)
        where = data.get('where',None)
        result = app.config['cursor'].get_one_result('project_apply',fields,where)
        #id转换成名字
        id2name_project=util.getinfo('project',['id','name'])
        result['project_name'] = id2name_project[str(result['project_id'])] 
        result['apply_date']=str(result['apply_date'])

        util.write_log('api').info(username, 'get one apply detail success')
        return json.dumps({'code':0,'result':result})
    except:
        util.write_log('api').error("get  apply detail faild : %s"  %  traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'任务详情获取失败!'})

#仿真发布 打上version版本号,触发仿真代码脚本,执行代码同步，同时更新status为2 并插入一条记录到project_deploy,状态为2
@jsonrpc.method('apply.update')
@auth_login
def apply_emulation(auth_info,**kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    try:
        data = request.get_json()['params']
        where = data.get('where',None)                   #传递过来测试打上的version，申请项目的ID
        data = data.get('data',None)
        where = {'id':int(where['id'])}                
        data =  {'version':data['version'],'status':2}
        apply_pub(username,data,where)
        return json.dumps({'code':0,'result':'emulation success'})
    except:
        util.write_log('api').error("apply.emulation get failed : %s" %  traceback.format_exc())
        return json.dumps({'code':1, 'errmsg':'仿真发布失败~!'})

#仿真失败，取消
@jsonrpc.method('apply.cancel')
@auth_login
def apply_cancel(auth_info,**kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    try:
        pid = kwargs.get('where')
        pid = pid['id']
        data,where = {'status':3},{'id':pid},
        apply_pub(username,data,where)
        return json.dumps({'code':0,'result':'cancel success'})
    except:
        util.write_log('api').error("apply.cancel get failed : %s" % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'取消仿真发布失败'})


#仿真测试成功，正式上线
@jsonrpc.method("apply.success")
@auth_login
def apply_success(auth_info,**kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    try:
        pid = kwargs.get('where')
        pid = pid['id']
        data,where = {'status':4},{'id':pid}
        apply_pub(username,data,where)
        return json.dumps({'code ':0,'result':'apply success'})
    except: 
        util.write_log('api').error("apply success  get failed : %s" % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'正式上线失败,请联系运维人员!'})


#上线历史记录查询
@jsonrpc.method("deploy.getlist")
@auth_login
def deploy_list(auth_info,**kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    try:
        fields = ['id','project_id','applicant','version','commit','apply_date','status']
        result = app.config['cursor'].get_results('project_deploy',fields) 
        #id转换成名字
        id2name_project=util.getinfo('project',['id','name'])
        for res in result:
            res['project_name'] = id2name_project[str(res['project_id'])]           
            res['apply_date']=str(res['apply_date'])
       
        util.write_log('api').info(username, 'get deploy list success!')
        return  json.dumps({'code':0, 'result':result, 'count':len(result)})
    except:
        util.write_log('api').error("select deploy list error:%s" % traceback.format_exc())
        return json.dumps({'code': 1, 'errmsg': '获取上线历史记录失败'})

#上线历史记录详情
@jsonrpc.method("deploy.get")
@auth_login
def deploy_get(auth_info, **kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    try:
         data = request.get_json()['params']
         where = data.get('where',None)
         fields = ['id', 'project_id','info','applicant','version','commit','apply_date','status','detail']
         result = app.config['cursor'].get_one_result('project_deploy', fields, where)
         #id转换成名字
         id2name_project=util.getinfo('project',['id','name'])
         result['project_name'] = id2name_project[str(result['project_id'])]           
         result['apply_date']=str(result['apply_date'])
         util.write_log('api').info(username, "get deploy  success!")
         util.write_log('api').info(result)
         return json.dumps({'code':0, 'result':result,})
    except:
        util.write_log('api').error("get deploy error:%s" % traceback.format_exc())
        return json.dumps({'code': 1, 'errmsg': "获取版本上线历史记录失败"})

