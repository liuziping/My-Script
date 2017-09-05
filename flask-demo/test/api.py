#!/usr/bin/env python
#encoding:utf-8
__author__ = 'bianji'
import json
import os
import imp

class AuthLoad(object):
    moduledir = '/home/liuziping/flask-demo/test'
    def __init__(self,module_name):
        self.module_name = module_name
        self.module = None
        self.method = None

    def isValidMethod(self,func):
        self.method = func
        return hasattr(self.module,func)

    def isValidModule(self):
        '''判断模块是否可加载'''
        return self._load_module()

    def getCallMethod(self,func):
        '''返回可执行的方法'''

        return self.method
    def _load_module(self):
        ret = False
        for filename in os.listdir(self.moduledir):
            if filename.endswith('.py'):
                mname = filename.strip('.py')
                if mname == self.module_name:
                    fp,pathname,desc = imp.find_module(self.module_name,[self.moduledir])
                    if not fp:
                        continue
                    else:
                        try:
                            self.module = imp.load_module(mname,fp,pathname,desc)
                            ret = True
                        except:
                            fp.close()
                        break
        return ret



class Response(object):
    '''response对象'''
    def __init__(self):
        self.data = None
        self.errorCode = 0
        self.errorMessage = None



class JsonRpc(object):
    def __init__(self,json_data):
        self.response = Response()
        self.json_data = json.loads(json_data)

    def execute(self):
        '''执行指定的方法，返回执行结果'''
        if self.json_data.get('id') is None:
            self.jsonErrorr(id='Null',errorCode=-1,data='json data not fount id')
            return self.response
        if self.validate():
            print '验证通过'
            module,func = self.json_data['method'].split('.')[0],self.json_data['method'].split('.')[1]
            self.callMethod(module,func,self.json_data['params'])
            self.processResult()
            return self.response
        else:
            return self.response

    def callMethod(self,module,func,params):
        '''加载模块，验证权限，执行方法，返回response'''
        at = AuthLoad(module)
        if not at.isValidModule():
            self.response.errorMessage = 'No module named %s' % module
            self.response.errorCode = -100
            return False
        if not at.isValidMethod(func):
            self.response.errorMessage = 'Module object has no attribute %s' % func
            self.response.errorCode = -100
            return False

    def requiresAuthentication(self,module,func):
        '''判断需要执行的API是否需要验证权限'''
        auth_dict = {'user':['login','logout'],
                     'idc':['get','update']}
        if module in auth_dict and func in auth_dict[module]:
            return True
        else:
            self.response = self.jsonErrorr(id=self.json_data['id'],
                                            errorCode=403,
                                            data='API forbidden')
            return False

    def validate(self):
        '''验证json数据'''
        if self.json_data['jsonrpc'] != '2.0':
            self.jsonErrorr(id=self.json_data['id'],
                            errorCode=-5,
                            data='jsonrpc version is error')
            return False
        if '.' in self.json_data['method'] and len(self.json_data['method'].split('.')) == 2:
            pass
        else:
            self.jsonErrorr(id=self.json_data['id'],
                            errorCode=-5,
                            data='method error')
            return False
        if 'params' not in self.json_data:
            self.jsonErrorr(id=self.json_data['id'],
                            errorCode=-5,
                            data='not found params')
            return False
        if not isinstance(self.json_data['params'],dict):
            self.jsonErrorr(id=self.json_data['id'],
                           errorCode=-5,
                           data='params type error')
            return False
        return True

    def jsonErrorr(self,id,errorCode,data=None):
        '''处理json错误'''
        format_error = {
            'errorCode':errorCode,
            'id':id,
            'data':data
        }
        self.response = format_error

    def processResult(self):
        '''处理执行后返回的结果'''
        if self.response.errorCode != 0:
            self.jsonErrorr(id=self.json_data['id'],
                            errorCode=self.response.errorCode,
                            data = self.response.errorMessage)
        else:
            format_Resp = {
                "jsonrpc":'2.0',
                "result":'OK',
                "id":self.json_data['id']
            }
            self.response = format_Resp

    def isError(self):
        '''返回是否有错误'''



if __name__ == '__main__':
    data = {
        "jsonrpc": "2.0",
        "id":2,
        "method":"idc.get",
        "auth":None,
        "params":{}
    }
    test = JsonRpc(json.dumps(data))
    print test.execute()
   # at = AuthLoad('idc')
   # at.isValidModule()
   # print at.isValidMethod('get')
