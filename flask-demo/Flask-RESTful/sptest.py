#!/usr/bin/env python 

import ansible.runner
name = "test.sh"
runner = ansible.runner.Runner(
   module_name='shell',
   module_args='sh /usr/local/sbin/%s' % name,
   pattern='dev-online',
   forks=10
)
data = runner.run()
print data

