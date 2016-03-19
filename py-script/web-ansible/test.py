#!/usr/bin/env  python

import os
import time
import redis
import json

class CallbackModule(object):
     def runner_on_ok(self,host,res):
        result={}
        fields=['cmd','start','end','delta','stdout']
        r = dict((k,res[k])  for k in fields)
        result[host]=r
        print  json.dumps(result,indent=4) 

     def runner_on_failed(self,host,res,ignore_errors=False):
        error={} 
        fields=['cmd','start','end','delta','stderr']
        r = dict((k,res[k]) for k in fields)
        error[host]=r
        print  json.dumps(error,indent=4) 

     def runner_on_skipped(self, host, item=None):
        print  "%s skipped" % host 



