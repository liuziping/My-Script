#!/bin/env python
# -*- encoding: utf-8 -*-
from api import app
import os,sys
import db,utils

#session使用需要设置secret_key
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#导入自定义的各种配置参数，最终参数以字典形式返回
config = utils.get_config('api')
#print config
#将参数追加到app.config字典中，就可以随意调用了
app.config.update(config)

#实例化数据库类，并将实例化的对象导入配置
app.config['cursor'] = db.Cursor(config)
print app.config

if __name__ == '__main__':
    app.run(host=config.get('bind', '0.0.0.0'),port=int(config.get('port')), debug=True)
