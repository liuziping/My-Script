#!/usr/bin/env python
#coding:utf-8
from flask import  request
from . import app , jsonrpc
from auth import auth_login
import json, traceback
import util
import time,os

# 这里是关于项目的增删改查

@jsonrpc.method('project.create')
@auth_login
def project_create(auth_info, **kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    if '1' not in  auth_info['r_id']:
        return json.dumps({'code': 1,'errmsg':'you not admin,no power'})
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
        data['create_date'] = time.strftime('%Y-%m-%d')
        app.config['cursor'].execute_insert_sql('project', data)
        # 信息入库后，调用函数，让gitolite生效，返回结果成功，则发送邮件
        res = gitolite()
        if res['code'] == 1:
            return json.dumps(res)
        # 获取当前项目的所有人，为下面发邮件准备数据
        members,principal = util.project_members()   
        sender = members[data['name']]
        # 发邮件
        util.write_log('api').info("%s:create project %s scucess" %  (username,data['name']))
        return json.dumps({'code':0,'result':'create project %s scucess' % data['name']})
    except:
        util.write_log('api').error("create project error: %s" % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'create project fail'})

@jsonrpc.method('project.getlist')
@auth_login
def project_select(auth_info,**kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    try:
        output = ['id','name','path','principal','p_user','p_group','is_lock','comment']
        data = request.get_json()['params']
        fields = data.get('output', output)
          
        # 查询用户表，生成id2name的字典
        users=util.getinfo('user',['id', 'name'])

        # 查询角色表，生成id2name的字典
        roles=util.getinfo('role',['id', 'name'])

        # 管理员查询项目表，把项目表中p_uesr,p_group,principal的ID 转为name
        # 结果:[{'id':1,'name':'devops','principal':'pc','p_user':'pc,wd'....},......]
        projects = app.config['cursor'].get_results('project', fields)
        for p  in projects:  # 循环项目列表，判断项目表中的p_user的id是否存在，如果存在则id2name
            p['principal'] = ','.join([users[x] for x in  p['principal'].split(',') if x in users])
            p['p_user'] =  ','.join([users[u] for u in p['p_user'].split(',') if u in users])
            p['p_group'] =  ','.join([roles[r] for r in p['p_group'].split(',')  if r in roles])
        
        # 普通用户只能查看其有权限的项目,上面总结果集projects中过滤
        if '1' not in  auth_info['r_id']:  
            p = util.user_projects(username)  # 查出用户的项目id2name{'1':'devops','2':'test'}
            projects = [pro for pro in projects for pid in p.keys() if pid==pro['id']] # 获取项目的详情 
        
        util.write_log('api').info('%s:select project list success' % username)
        return json.dumps({'code':0,'result':projects,'count':len(projects)})
    except:
        util.write_log('api').error("select project list error: %s"  %  traceback.format_exc())
        return json.dumps({'code': 1,'errmsg':'get projectlist failed'})

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
            util.write_log('api').info("%s:select project by id success" % username)
            return json.dumps({'code':0,'result':result})
    except:
        util.write_log('api').error('select project by id error: %s'  % traceback.format_exc())
        return  json.dumps({'code':1,'errmsg':'get project failed'})
# 更新操作，从API的角度考虑也需要对传入的值eg:p_user判断是否存在，但考虑到应用场景都是web，就不写了
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
        res = gitolite()
        if res['code'] == 1:
            return json.dumps(res)
        util.write_log('api').info('%s:update project success!' % username)
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
        util.write_log('api').info('%s:delete project successed' % username)
        return json.dumps({'code' :0,'result':'delete project scucess'})
    except:
        util.write_log('api'). error('delete project error: %s' %  traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'delete project failed'})  


# 查询某个用户所拥有的项目列表,已经整合到getlist中
'''
@jsonrpc.method('userprojects.getlist')
@auth_login
def userprojects(auth_info,**kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)             
    username = auth_info['username']
    try:
        res = util.user_projects(username) #{'1':'devops','2':'test'}
        return json.dumps({'code': 0, 'result': res})
    except:
        util.write_log('api').error("调用userproject函数失败: %s" % traceback.format_exc())
        return json.dumps({'code': 1, 'errmsg': '查询项目列表错误'})
'''
# 从project库中读取项目信息，生成git配置文件，实现对运维平台和git仓库打通

@app.route('/api/gitolite',methods=['GET'])
def git_api():
    res = gitolite()
    return  json.dumps(res)

'''
渲染gitolite配置文件及推送接口
Use:
    curl http://127.0.0.1:1000/api/gitolite
'''
def gitolite():
    git_confile = app.config['git_confile']
    api_dir = os.path.dirname(os.path.realpath(__file__))
    script_dir =  os.path.join(api_dir.rstrip('api'),'script')
    projects,pro_pri = util.project_members() 
    group = util.role_members()
    try :
        # 将项目和用户信息写入配置文件中
        with open(git_confile,'w') as f:
                str0 = ""
                for k,v in group.items():
                    str0 += "@%s = %s\n" % (k," ".join(v))
                f.write(str0)
                f.write("\n")

                str1= ""
                for k,v in projects.items():
                    # 由于projests中存放了项目所有的成员，包括负责人。需要把负责人剔除        
                    v = list(set(v)-set(pro_pri[k])) 
                    str1 += "repo %s \n" % k
                    str1 += " RW+ = %s \n" % ' '.join(pro_pri[k])   # 负责人的权限最大
                    if v:           # 如果项目除了负责人外，有其他成员，则设置成员的权限
                        str1 += " -  master = %s \n" %(' '.join(v)) # 项目成员无权操作master分支
                        str1 += " RW = %s \n" %(' '.join(v))        # 项目成员可以操作其他分支
                f.write(str1)
        # git add/commit/push生效.路径暂时写死，定版前修改
        # stdout=util.run_script_with_timeout("sh %s/git.sh" % script_dir)
        # print stdout
        return {'code':0,'result':"git操作成功"}
    except:
        util.write_log('api'). error("get config error: %s" % traceback.format_exc())
        return {'code':1,'errmsg':"get config error"}

