#!/bin/env python
# -*- encoding: utf-8 -*-

import os, os.path
import time,json
import base64
import hashlib
import traceback
import ConfigParser
import logging,logging.config
from api import app

def get_config(service_conf, section=''):
    config = ConfigParser.ConfigParser()
    config.read(service_conf)

    conf_items = dict(config.items('common')) if config.has_section('common') else {}
    if section and config.has_section(section):
       conf_items.update(config.items(section))
    return conf_items

def write_log(loggername):
    work_dir = os.path.dirname(os.path.realpath(__file__))
    log_conf= os.path.join(work_dir, 'conf/logger.conf')
    logging.config.fileConfig(log_conf)
    logger = logging.getLogger(loggername)
    return logger


def get_validate(username, uid, role, fix_pwd):
    t = int(time.time())
    validate_key = hashlib.md5('%s%s%s' % (username, t, fix_pwd)).hexdigest()
    return base64.b64encode('%s|%s|%s|%s|%s' % (username, t, uid, role, validate_key)).strip()

def validate(key, fix_pwd):
    t = int(time.time())
    key = base64.b64decode(key)
    x = key.split('|')
    if len(x) != 5:
        write_log('api').warning("token参数数量不足")
        return json.dumps({'code':1,'errmsg':'token参数不足'})
    if t > int(x[1]) + 2*60*60:
        write_log('api').warning("登录已经过期")
        return json.dumps({'code':1,'errmsg':'登录已过期'})
    validate_key = hashlib.md5('%s%s%s' % (x[0], x[1], fix_pwd)).hexdigest()
    if validate_key == x[4]:
        write_log('api').info("api认证通过")
        return json.dumps({'code':0,'username':x[0],'uid':x[2],'r_id':x[3]})
    else:
        write_log('api').warning("密码不正确")
        return json.dumps({'code':1,'errmsg':'密码不正确'})

def check_name(name):
    if isinstance(name, str) or isinstance(name, unicode):
        return name.isalnum() and len(name) >= 2
    else:
        return False

def getinfo(table_name, fields):
        '''
        实现查询表中多任意两列，并将结果拼接为字典
        fields为列表存两个字段,格式为 ['field1','field2'], 例如['id','name'],['name','r_id']
        结果一，两列都是字符串如：用户id2name {'1':'tom','2','jerry'}; 组信息id2name {'1':'sa','2':'ask'}
        结果二，第二列是个列表如：用户name2r_id：{u'wd': [u'1', u'2'], u'admin': [u'1', u'2', u'4', u'3']}

        '''
        result = app.config['cursor'].get_results(table_name,fields) #[{'id':1,'name':'wd'},.....]
        if fields[1] in ['r_id','p_id','p_user','p_group']:  #第二列如果是列出的几项。则把字符串换成列表
	        result = dict((str(x[fields[0]]), x[fields[1]].split(',')) for x in result)
        else:
	        result = dict((str(x[fields[0]]), x[fields[1]]) for x in result)
        return result


#获取一个组里面的用户成员,以用户表的r_id,反推组成员，故如果组内无成员，则这个组就不会返回
def role_members():
    users = getinfo('user',['id','username'])   #{'1':'wd','2':'pc'}
    roles = getinfo('role',['id','name'])   #{'1':'sa','2':'dba','3':'dev'}
    r_id = getinfo('user',['id','r_id'])     #{'1':['1','2'],'2':['2'.'3']......}

    g = {}
    for uid, rids in r_id.items():
        for rid in rids:
            if uid not in users or rid not in roles:                                                
               continue
            if roles[rid] not in g:
                g[roles[rid]] = []
            g[roles[rid]].append(users[uid])
    return g
    #print g    #{'sa': ['wd'], 'dba': ['wd','pc'], 'dev': ['pc']}

#获取一个项目中所有的用户成员（用户和组中的成员要去重）结果格式： {'devops':['wd','pc'],'test':['wd','rock']}
def project_members():
        users = getinfo('user',['id','username'])   #{'1':'wd','2':'pc'}
        roles = getinfo('role',['id','name'])   #{'1':'sa','2':'dba','3':'dev'}
        r_users = role_members()        #{'sa': ['wd'], 'dba': ['wd','pc'], 'dev': ['pc']}
        result = app.config['cursor'].get_results('project',['id','name','principal','p_user','p_group']) 
        #result=[{'id':'1','name':'devops','principal':'1','p_user':'1,2','p_group':'1,3'},......]
        projects={}
        for p in result:
            projects[p['name']]=[]
            for pri in p['principal'].split(','):
                if pri in users:
                    projects[p['name']].append(users[pri]) 
            for u in p['p_user'].split(','):
                if u in users:
                    projects[p['name']].append(users[u]) 
            for g in p['p_group'].split(','):
                 if g in roles:
                    projects[p['name']] + r_users.get(roles[g],[]) #由于r_users不保存空组的信息，但项目表可能选择了空组，r_users[role]就会出现keyerro.故遇到这种情况取空列表
            projects[p['name']] = list(set(projects[p['name']])) #将p_user和p_group中的用户去重复
        
        return projects

#返回用户所拥有权限的项目，结果为：{"1": "test", "3": "devops"}
def user_projects(name):
    members = project_members()       #{'devops':['wd','pc'],'test':['wd','rock']}
    projects = getinfo('project',['name','id'])   #{'devops':'1','test':'2'}
    return dict([(projects[x],x) for x in members if name in members[x]] )
