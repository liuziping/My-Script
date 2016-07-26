#/usr/bin/env python
#coding:utf-8

import utils   
utils.write_log('web').info("hello")
utils.write_log("api").info("hello world")

conf = utils.get_config("api")
print conf 

token = utils.get_validate("wd","1","sa","123456")
print token 
print utils.validate(token,"123456")
