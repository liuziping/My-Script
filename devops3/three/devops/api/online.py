#!/usr/bin/env python
#coding: utf-8
from flask import  request
from . import app, jsonrpc
import logging, time
import json, traceback
from auth import auth_login
import utils


# 申请列表的处理会同时操作两个表
def apply_pub(username,data,where):
    # 更新project_apply表
    app.config['db'].execute_update_sql('project_apply',data,where)
    utils.write_log('api').info("%s:success and update project_apply status %s" % (username,data['status']))

    # 同时将本次操作插入到project_deploy中
    fields = ['project_id','info','applicant','status','apply_date','version','commit','detail']  
    result = app.config['db'].get_one_result('project_apply',fields,where)
    app.config['db'].execute_insert_sql('project_deploy',result)
    utils.write_log('api').info("%s:success and insert project_deploy status  %s"  % (username,data['status']))

# 创建申请任务列表
@jsonrpc.method('apply.create') 
@auth_login
def apply_create(auth_info, **kwargs):
    username = auth_info['username']
    r_id = auth_info['r_id']
    field = ['project_id','info','applicant','commit','apply_date','status','detail']
    try:
        data = request.get_json()['params']  # project_id,project_name,applicant,info,detail
        data['commit']='11111'               # 脚本获取最新的commit
        data['apply_date'] = time.strftime('%Y-%m-%d %H:%M')
        data['status'] = 1                   # 项目申请后状态变为1，
        data['applicant'] = username 
        where = {"project_id":int(data['project_id'])}
        data.pop('project_username')         # 因为申请表单里面有项目名,数据库里存的上id,所以要除掉
        res = app.config['db'].get_one_result('project_apply',field,where)
        if res and res['status'] in (1,2):
            return json.dumps({'code': 1, 'errmsg': '目前项目状态不可申请'})
        if not res: 
            app.config['db'].execute_insert_sql('project_apply', data)
        else:
            app.config['db'].execute_update_sql('project_apply',data,where)
        app.config['db'].execute_insert_sql('project_deploy',data)  
        utils.write_log('api').info('%s:项目申请成功' % username)
        return json.dumps({'code':0,'result':'项目申请成功'})    
    except:
        utils.write_log('api').error('project apply error: %s' % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'项目申请失败'})


# 申请列表，任务列表
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
        # 申请者看到的项目列表
        applylist = app.config['db'].get_results('project_apply',fields)     
        
        # 审核者看到的申请列表，只显示申请中和审核中的项目
        where = {'status':['1','2']}
        result = app.config['db'].get_results('project_apply',fields,where) 

        # id转换成名字在前端页面展示，同事时间类型需要转为字符串之后才能被json传输
        id2name_project=utils.getinfo('project',['id','name'])
        for res in applylist:
            res['project_name'] = id2name_project[str(res['project_id'])]           
            res['apply_date']=str(res['apply_date'])
        for res in result:
            res['project_name'] = id2name_project[str(res['project_id'])]           
            res['apply_date']=str(res['apply_date'])

        utils.write_log('api').info('%s:get apply list success!' % username)
        return  json.dumps({'code':0,'data': applylist, 'result':result,'count':len(result)})
    except:
        utils.write_log('api').error("select apply list error:%s" % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'任务列表获取失败!'})

# 申请列表，详情按钮
@jsonrpc.method('apply.get')
@auth_login
def apply_one(auth_info,**kwargs):
    username = auth_info['username']
    try:
        data = request.get_json()['params']
        output = ['id','project_id','info','applicant','version','commit','apply_date','status','detail']
        fields = data.get('output', output)
        where = data.get('where',None)
        result = app.config['db'].get_one_result('project_apply',fields,where)
        # id转换成名字
        id2name_project=utils.getinfo('project',['id','name'])
        result['project_name'] = id2name_project[str(result['project_id'])] 
        result['apply_date']=str(result['apply_date'])

        utils.write_log('api').info('%s:get one apply detail success' % username)
        return json.dumps({'code':0,'result':result})
    except:
        utils.write_log('api').error("get apply detail faild : %s" % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'任务详情获取失败!'})


# 仿真发布 打上version版本号,触发仿真代码脚本,执行代码同步，同时更新status为2 并插入一条记录到project_deploy,状态为2
@jsonrpc.method('apply.update')
@auth_login
def apply_emulation(auth_info,**kwargs):
    username = auth_info['username']
    try:
        data = request.get_json()['params']
        where = data.get('where',None)                   # 传递过来测试打上的version，申请项目的ID
        data = data.get('data',None)
        where = {'id':int(where['id'])}                
        data =  {'version':data['version'],'status':2}
        # 调用执行脚本，将代码同步到仿真服务器，然后根据返回结果执行下面内容,此处需要根据where条件拿到项目的详细信息，传给脚本
        
        apply_pub(username,data,where)
        return json.dumps({'code':0,'result':'emulation success'})
    except:
        utils.write_log('api').error("apply.emulation get failed : %s" %  traceback.format_exc())
        return json.dumps({'code':1, 'errmsg':'仿真发布失败~!'})

# 仿真失败，取消
@jsonrpc.method('apply.cancel')
@auth_login
def apply_cancel(auth_info,**kwargs):
    username = auth_info['username']
    try:
        pid = kwargs.get('where')
        pid = pid['id']
        data,where = {'status':3},{'id':pid},
        apply_pub(username,data,where)
        return json.dumps({'code':0,'result':'cancel success'})
    except:
        utils.write_log('api').error("apply.cancel get failed : %s" % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'取消仿真发布失败'})



# 仿真测试成功，正式上线
@jsonrpc.method("apply.success")
@auth_login
def apply_success(auth_info,**kwargs):
    username = auth_info['username']
    try:
        pid = kwargs.get('where')
        pid = pid['id']
        data,where = {'status':4},{'id':pid}
        # 调用执行脚本，将代码同步到正式服务器，然后根据返回结果执行下面内容,此处需要根据where条件拿到项目的详细信息，传给脚本
        apply_pub(username,data,where)
        return json.dumps({'code':0,'result':'apply success'})
    except: 
        utils.write_log('api').error("apply success  get failed : %s" % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'正式上线失败,请联系运维人员!'})


# 上线历史记录查询
@jsonrpc.method("deploy.getlist")
@auth_login
def deploy_list(auth_info,**kwargs):
    username = auth_info['username']
    try:
        fields = ['id','project_id','applicant','version','commit','apply_date','status']
        result = app.config['db'].get_results('project_deploy',fields) 
        # id转换成名字
        id2name_project=utils.getinfo('project',['id','name'])
        for res in result:
            res['project_name'] = id2name_project[str(res['project_id'])]           
            res['apply_date']=str(res['apply_date'])
       
        utils.write_log('api').info('%s:get deploy list success!' % username)
        return  json.dumps({'code':0, 'result':result, 'count':len(result)})
    except:
        utils.write_log('api').error("select deploy list error:%s" % traceback.format_exc())
        return json.dumps({'code': 1, 'errmsg': '获取上线历史记录失败'})

# 上线历史记录详情
@jsonrpc.method("deploy.get")
@auth_login
def deploy_get(auth_info, **kwargs):
    username = auth_info['username']
    try:
         data = request.get_json()['params']
         where = data.get('where',None)
         fields = ['id', 'project_id','info','applicant','version','commit','apply_date','status','detail']
         result = app.config['db'].get_one_result('project_deploy', fields, where)
         # id转换成名字
         id2name_project=utils.getinfo('project',['id','name'])
         result['project_name'] = id2name_project[str(result['project_id'])]           
         result['apply_date']=str(result['apply_date'])
         utils.write_log('api').info("%s:get deploy  success!" % username)
         return json.dumps({'code':0, 'result':result})
    except:
        utils.write_log('api').error("get deploy error:%s" % traceback.format_exc())
        return json.dumps({'code': 1, 'errmsg': "获取版本上线历史记录失败"})

