#!/bin/env python
# -*- encoding: utf-8 -*-

import os, os.path
import time,json
import base64
import hashlib
import traceback
import ConfigParser
import logging,logging.config

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
    logger = logging.getLogger("web")
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
        return json.dumps({'code':0,'username':x[0],'uid':x[2],'role':x[3]})
    else:
        write_log('api').warning("密码不正确")
        return json.dumps({'code':1,'errmsg':'密码不正确'})

